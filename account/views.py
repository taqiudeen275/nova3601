from django.shortcuts import render,redirect,get_object_or_404,reverse
from .form import *
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  authenticate,login,logout
from django.contrib import messages



def loginView(request):
    if request.user.is_authenticated:
        return redirect(reverse('home:index'))   
    next1 = request.GET.get('next')
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            if username and password is not None:
                user = authenticate(username=username,password=password)
                login(request,user)
            
                if next1:
                    return redirect(next1)
            return redirect(reverse('blog:index'))
    context = {
        'form': form,
        'title': 'Login',
        
    }
    return render(request, 'account/login.html', context)



def signupView(request):
    form = SignupForm(request.POST or None)
    if request.user.is_authenticated:
        return redirect(reverse('blog:index'))
    if request.method == 'POST':
        if form.is_valid():
            user =form.save(commit= False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            user = authenticate(username=user.username, password=password)
            login(request, user)
            return redirect(reverse('blog:index'))
    context = {
        'form': form,
        'title': 'Register',
    }
    return render(request, 'account/register.html', context)


def logoutView(request):
    logout(request)
    return redirect(reverse('account:login'))

@login_required
def profile(request):
    form = ProfileForm(request.POST or None,request.FILES or None, instance=request.user)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    context = {
        'form': form,
        'title': 'Profile',
    }
    user = request.user
    return render(request, 'account/profile.html', context)

