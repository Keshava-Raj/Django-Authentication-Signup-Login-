from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required 




def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after registration
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'provider register.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('Email_id')
        password = request.POST.get('PPassword')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('sucssess')  # Replace 'home' with the URL name of your homepage
        else:
            messages.error(request, 'Invalid username or password')
    
    context = {
        'hidde': True,  # Navigation will be hidden
    }
    return render(request, 'providerLogin.html',context)



def home(request):
    return render(request, 'home.html')

@login_required
def sucssess(request):
    users = request.user  # it is pull out the logged-in user's details
    return render(request, 'order sucssess.html',  {'user': users} )


def logout_view(request):
    logout(request)
    return redirect('home')