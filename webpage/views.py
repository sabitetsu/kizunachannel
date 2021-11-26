from django.shortcuts import render

# Create your views here.

def jsonview(request):
    return render(request, 'json.html')