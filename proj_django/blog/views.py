from django.shortcuts import render

# Create your views here.
def blog(request):
    print("Request received")
    return render(request, 'blog/index.html')

def exemplo(request):
    print("Exemplo view")
    return render(request, 'blog/exemplo.html')