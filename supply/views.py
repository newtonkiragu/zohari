from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Image,Profile
from django.contrib.auth.decorators import  login_required
from django.contrib.auth.models import User

# Create your views here.
def contact(request):
    return render( request,'contact.html')

def about(request):
    return render( request,'about.html')

@login_required(login_url='/accounts/login/')
def index(request):

    images = Image.objects.all()
    users = User.objects.all()

    return render (request, 'all-supply/index.html',{"images":images},)

@login_required(login_url='/accounts/login/')
def profile(request,username):
    profile = User.objects.get(username=username)
    
    try:
        profile_details = Profile.get_by_id(profile.id)
    except:
        profile_details = Profile.filter_by_id(profile.id)
        
 