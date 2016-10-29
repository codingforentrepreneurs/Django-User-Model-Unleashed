from django.shortcuts import render

# Create your views here.


def home(request):
    if request.user.is_authenticated():
        print(request.user.profile.city)
    return render(request, "home.html", {})