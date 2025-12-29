from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import ResgisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = ResgisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('MyApp:index')
    form = ResgisterForm()
    return render(request, 'Users/register.html', {'form': form})