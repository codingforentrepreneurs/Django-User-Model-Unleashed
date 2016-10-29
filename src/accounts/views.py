from django.contrib.auth import login, get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

User = get_user_model()

from .forms import UserCreationForm, UserLoginForm

def home(request):
    if request.user.is_authenticated():
        print(request.user.profile.city)
    return render(request, "base.html", {})



def register(request, *args, **kwargs):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/login")
    return render(request, "accounts/register.html", {"form": form})


def user_login(request, *args, **kwargs):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username_ = form.cleaned_data.get('username')
        user_obj = User.objects.get(username__iexact=username_)
        login(request, user_obj)
        return HttpResponseRedirect("/")
    return render(request, "accounts/login.html", {"form": form})