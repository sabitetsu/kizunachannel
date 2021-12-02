import django_filters
from rest_framework import viewsets, filters

from .models import TalkModel
from .serializer import TalkModelSerializer

from django.shortcuts import render
import requests
import environ

env = environ.Env()
env.read_env('.env')

def wordRegist(request):
    print("word registration")
    return render(request, 'talkapp/wordregist.html')

def talkAPI(request):
    print("talkAPI request")
    API_key = env('API_KEY')
    print(API_key)
    word = "おはよう"
    if request.POST['word']:
        word = request.POST['word']
    url = 'https://api.a3rt.recruit.co.jp/talk/v1/smalltalk'
    query = {
        'apikey':API_key,
        'query':word
    }
    r = requests.post(url, {'apikey':API_key,'query':word})
    print(requests.get(url, params=query))
    print("r")
    print("response", r.json())
    result = [r.json()]
    
    return render(request, 'talkapp/talkAPI.html', {'word': word, 'result': result})




class TalkModelViewSet(viewsets.ModelViewSet):
    queryset = TalkModel.objects.all()
    serializer_class = TalkModelSerializer

