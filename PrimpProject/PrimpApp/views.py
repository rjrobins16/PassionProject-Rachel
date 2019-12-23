from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.db.models import Q
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import NewUserForm, SignInForm
from .models import Profile
from django.contrib.auth.models import User


# Create your views here.
from django.http import HttpResponse

def log_out(request):
    logout(request)
    return redirect("index")

def index(request):
    if request.method == "POST":
            newuser = NewUserForm(request.POST)
            if newuser.is_valid():
                logInUser = User.objects.create_user( username = request.POST['username'],
                                                    password=request.POST['password'],
                                                    first_name = request.POST['first_name'],
                                                    last_name = request.POST['last_name'],
                                                    email = request.POST['email'],
                                                    )
                login(request, logInUser)
                return redirect("home")
            else:
                context = {
                "errors": newuser.errors,
                "form": NewUserForm(),
                }
                return render (request, 'PrimpApp/index.html', context)
    else:
        context = {
        "form": NewUserForm()
        }
        return render(request, 'PrimpApp/index.html',context)



def log_in(request):
    if request.method == "POST":
        logInUser = authenticate(username=request.POST['username'], password=request.POST["password"])
        if logInUser is not None:
            login(request, logInUser)
            return redirect("home")
        else:
            messages.error(request, "Wrong username or password")
            return redirect("log_in")
    context = {
        "form": SignInForm()
    }
    return render(request, "PrimpApp/log_in.html", context)

def home(request):
    return render(request, "PrimpApp/home.html")