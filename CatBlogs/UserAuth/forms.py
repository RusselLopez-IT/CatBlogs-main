from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from UserAuth.models import CustomUser

class registrationform(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name')

class additionalinfo(forms.ModelForm):
    profile_picture = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    class Meta:
        model = CustomUser
        fields = ('address', 'sex', 'profile_picture')

class loginform(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('email',)