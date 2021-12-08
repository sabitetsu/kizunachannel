from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def fav(request):
    return render(request, 'fav.html')