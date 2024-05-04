from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.views import View






def registration_view(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            del form.cleaned_data['confirm_password']
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('user:login')
    return render(request, "accounts/sign-up.html", {'form': form})



def login_view(request):
    if request.user.is_authenticated:
        return redirect("e_commerce:home")
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("e_commerce:home")

            else:
                messages.info(request, "Username or password is incorrect")
    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect("user:login")

def check_username(request):
    username = request.POST.get("username")
    print('HTMX event fired 1')
    if get_user_model().objects.filter(username=username).exists():
        print('HTMX event fired 2')
        return HttpResponse("This username already exists")
    else:
        print('HTMX event fired 3')
        return HttpResponse("This username not found")