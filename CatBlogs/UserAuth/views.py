from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model, logout
from .forms import registrationform, additionalinfo, loginform
from .models import Article

def registerUser(request):
    if request.method == 'POST':
        form = registrationform(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('additionalInfo')
    else:
        form = registrationform()

    return render(request, 'register.html', {'form': form})


def loginUser(request):
    if request.method == 'POST':
        form = loginform(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('index') 
    else:
        form = loginform()
    return render(request, 'login.html', {
        'form': form
        })

def additional(request):
    if request.method == 'POST':
        form = additionalinfo(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = additionalinfo()

    return render(request, 'additional.html', {'form': form})

def profile(request):
    user_articles = Article.objects.filter(author=request.user)
    return render(request, 'Profile/UserProfile.html', {'articles': user_articles})