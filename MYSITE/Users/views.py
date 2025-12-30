from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, authenticate
from django.contrib import messages
from .forms import ResgisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = ResgisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    form = ResgisterForm()
    return render(request, 'Users/register.html', {'form': form})

def logout_views(request):
    logout(request)
    return render(request, 'Users/logout.html')

@login_required
def profile(request):
    return render(request, 'Users/profile.html')