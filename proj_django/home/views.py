from django.shortcuts import render


# Create your views here.
def home(request):
    print("Home")
    context = {"title": "Home Page", "message": "Welcome to the Home Page!"}
    return render(request, "home/index.html", context)
