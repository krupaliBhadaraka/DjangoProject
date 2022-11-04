from django.shortcuts import render
from django.http import HttpResponse
from LoginApp.forms import LoginForm
from LoginApp.models import LoginModel
from passlib.hash import pbkdf2_sha256
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def index(request):
    return HttpResponse("<h1>Welcome</h1>")


def login_view(request):
    login_form = LoginForm()
    if request.method == 'POST':
        password = request.POST.get('password')
        username = request.POST.get('username')
        encypt_pwd = LoginModel.objects.get(username=username)
        user_login = pbkdf2_sha256.verify(password, encypt_pwd.password)
        if user_login:
            return HttpResponse("Logged in")
        else:
            return HttpResponse("Something went wrong")
    return render(request, 'login.html', {'forms': login_form})


def register_view(request):
    login_form = LoginForm()
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        password = request.POST['password']
        username = request.POST['username']
        password = pbkdf2_sha256.encrypt(password)
        if login_form.is_valid():
            LoginModel.objects.create(username=username, password=password)
            return index(request)
    return render(request, 'register.html', {'forms': login_form})
