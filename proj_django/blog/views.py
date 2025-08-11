from blog.data import posts
from django.shortcuts import render

# Create your views here.
def blog(request):
    print("Request received")
    context = {"title": "Blog Page", "posts": posts}
    return render(request, 'blog/index.html', context)

def exemplo(request):
    print("Exemplo view")
    context = {"title": "Exemplo Page", "message": "This is an example page!"}
    return render(request, 'blog/exemplo.html', context)

def post(request, id):
    print(f"Post requested with ID: {id}")
    context = {"posts": posts}
    return render(request, 'blog/index.html', context)