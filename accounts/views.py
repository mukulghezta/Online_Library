from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import auth, User
from django.contrib import messages


def signup_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Aready in Use")

            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email ID Aready in Use")
            else:
                user = User.objects.create_user(username=username,password=password,email=email)
                user.save()
                if user is not None:
                    auth.login(request,user)
                messages.info(request,"You have successfully signed up and are now logged in as {}!!!".format(username))
                return redirect("books_cds:home")
        else:
            messages.info(request,"Both Password fields are not matching")
        return render(request, 'accounts/signup.html')
    else:
        return render(request, 'accounts/signup.html')


def login_view(request):
    if request.method == "POST":
        uname = request.POST["username"]
        pwd1 = request.POST['pwd']
        
        user = auth.authenticate(username=uname,password=pwd1)
        if user is not None:
            auth.login(request,user)
            messages.info(request,"You are now logged in as {}!!!".format(uname))
            return redirect('books_cds:home')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('accounts:login')
    
    else:
        return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('books_cds:home')