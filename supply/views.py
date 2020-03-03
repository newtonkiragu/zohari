from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def index(request):
    images = Product.objects.all()
    users = User.objects.all()

    return render(request, 'all-supply/index.html', {"images": images}, )


@login_required(login_url='/accounts/login/')
def profile(request, username):
    profile = User.objects.get(username=username)

    try:
        profile_details = Profile.get_by_id(profile.id)
    except:
        profile_details = Profile.filter_by_id(profile.id)


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
