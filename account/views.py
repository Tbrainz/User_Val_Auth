from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegUser

# Create your views here.

def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('account:dashboard')
        # else:
        #     return redirect('account:login')


    return render(request, 'account/index.html')

# dashboard with login_required decorator
@login_required(login_url='account:login')
def dashboard(request):
    return render(request, 'account/dashboard.html')

def logoutPage(request):
    logout(request)
    return redirect('account:login')

def register(request):
    form = RegUser()

    if request.method == 'POST':
        form = RegUser(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            user = authenticate(request, username = user.username, password = request.POST['password1'])
            if user is not None:
                login(request, user)
                return redirect('account:dashboard')
    return render(request, 'account/register.html', {'form':form})