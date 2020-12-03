from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Product, Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q


# Create your views here.
def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


class HomePageView(ListView):
    model = Product
    template_name = 'product/index.html'


class ProductDetail(DetailView):
    model = Product
    template_name = 'product/product_detail.html'


class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'


@login_required(login_url='/accounts/login/')
def profile(request, username):
    user = User.objects.get(username=username)

    try:
        profile_details = Profile.get_by_id(user.id)
    except:
        profile_details = Profile.filter_by_id(user.id)
    return render(request, 'registration/profile.html', {"object": user})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registration_form.html', {'form': form})


class SearchResultsView(ListView):
    model = Product
    template_name = 'search_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(
            Q(item_name__icontains=query) | Q(
                item_description__icontains=query)
        )
        return object_list
