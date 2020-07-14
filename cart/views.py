from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from cart.models import Cart, Order
from shop.models import Product


@login_required(login_url='/accounts/login/')
def add_to_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_item, created = Cart.objects.get_or_create(
        item=item,
        user=request.user
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.order_items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, f"This {item.item_name} quantity was updated.")
            return redirect("cart-home")
        else:
            order.order_items.add(order_item)
            messages.info(request, f"This {item.item_name} was added to your cart.")
            return redirect("landing_page")
    else:
        order = Order.objects.create(
            user=request.user)
        order.order_items.add(order_item)
        messages.info(request, f"This {item.item_name} was added to your cart.")
        return redirect("landing_page")


@login_required(login_url='/accounts/login/')
def decrease_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.order_items.filter(item__slug=item.slug).exists():
            order_item = Cart.objects.filter(
                item=item,
                user=request.user
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.order_items.remove(order_item)
                order_item.delete()
            messages.info(request, f"{item.item_name} quantity has updated.")
            return redirect("cart-home")
        else:
            messages.info(request, f"{item.item_name} quantity has updated.")
            return redirect("landing_page")
    else:
        messages.info(request, "You do not have an active order")
        return redirect("landing_page")


@login_required(login_url='/accounts/login/')
def remove_from_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    cart_qs = Cart.objects.filter(user=request.user, item=item)
    if cart_qs.exists():
        cart = cart_qs[0]
        # Checking the cart quantity
        if cart.quantity > 1:
            cart.quantity -= 1
            cart.save()
        else:
            cart_qs.delete()
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.orde_ritems.filter(item__slug=item.slug).exists():
            order_item = Cart.objects.filter(
                item=item,
                user=request.user,
            )[0]
            order.order_items.remove(order_item)
            messages.info(request, f"This {item.item_name} was removed from your cart.")
            return redirect("landing_page")
        else:
            messages.info(request, f"This {item.item_name} was not in your cart")
            return redirect("landing_page")
    else:
        messages.info(request, "You do not have an active order")
        return redirect("landing_page")


@login_required(login_url='/accounts/login/')
def cart_view(request):
    user = request.user

    carts = Cart.objects.filter(user=user)
    orders = Order.objects.filter(user=user, ordered=False)

    if carts.exists():
        order = orders[0]
        return render(request, 'cart/home.html', {"carts": carts, 'order': order})

    else:
        messages.warning(request, "You do not have an active order")
        return redirect("landing_page")
