from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View, UpdateView
from .models import Product, Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode

from shop.tokens import account_activation_token
from shop.forms import ProfileCreateForm, SignUpForm

# Create your views here.
def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


class HomePageView(ListView):
    model = Product
    template_name = 'product/index.html'


class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'

def product_detail(request, slug):
    objec = get_object_or_404(Product, slug=slug)
    template_name = 'product/product_detail.html'

    return render(request, template_name, context={'object': objec})



@login_required(login_url='/accounts/login/')
def profile(request, username):
    user = User.objects.get(username=username)

    try:
        profile_details = Profile.get_by_id(user.id)
    except:
        profile_details = Profile.filter_by_id(user.id)
    return render(request, 'registration/profile.html', {"object": user})


# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         p_form = ProfileCreateForm(request.POST, request.FILES)
#         if form.is_valid():
#             if p_form.is_valid():
#                 p_form.save()
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#         p_form = ProfileCreateForm(request.POST, request.FILES)
#     return render(request, 'registration/registration_form.html', {'form': form, 'p_form': p_form})

class ActivateAccount(View):

    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.profile.email_confirmed = True
            user.save()
            login(request, user)
            messages.success(request, ('Your account have been confirmed.'))
            return redirect('landing_page')
        else:
            messages.warning(request, ('The confirmation link was invalid, possibly because it has already been used.'))
            return redirect('landing_page')

# Sign Up View
class SignUpView(View):
    form_class = SignUpForm
    template_name = 'registration/registration_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
                
            user = form.save(commit=False)
            user.is_active = True # Deactivate account till it is confirmed. Set to True for now, default should be false
            user.save()

            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('emails/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)

            messages.success(request, ('Please Confirm your email to complete registration.'))

            return redirect('login')

        return render(request, self.template_name, {'form': form})

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
