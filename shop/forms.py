from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from shop.models import Profile

# Sign Up Form
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = [
            'username', 
            'email', 
            'password1', 
            'password2', 
            ]

class ProfileCreateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['profile_photo', 'bio', 'phone_number']