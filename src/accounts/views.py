from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

from .forms import UserCreationForm

def home(request):
    if request.user.is_authenticated():
        print(request.user.profile.city)
    return render(request, "home.html", {})



def register(request, *args, **kwargs):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/login")
    return render(request, "accounts/register.html", {"form": form})