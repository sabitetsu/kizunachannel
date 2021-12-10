import django_filters
from requests.api import request
from requests.models import Response
from rest_framework import serializers, viewsets, filters
import talkapp

from .models import TalkModel
from .serializer import TalkAPISerializer, TalkModelSerializer

from django.shortcuts import render
import requests
import environ
# import json

env = environ.Env()
env.read_env('.env')

def wordRegist(request):
    print("word registration")
    queryword = "なし"
    if 'regword' in request.GET:
        queryword = request.GET['regword']
    return render(request, 'talkapp/wordregist.html', {'query': queryword})

def kizuna(request):
    API_key = env('API_KEY')
    word = "やあ"
    if request.POST.get('word'):
        word = request.POST.get('word')
    url = 'https://api.a3rt.recruit.co.jp/talk/v1/smalltalk'
    query = {
        'apikey':API_key,
        'query':word
    }
    r = requests.post(url, query)
    try:
        result = [r.json()['results'][0]['reply']]
    except:
        result = ["よくわかんないです"]

    return render(request, 'talkapp/kizuna.html', {'reply': result[0]})

def talkAPI(request):
    print("talkAPI request")
    API_key = env('API_KEY')
    word = "ヌル"
    if request.POST.get('word'):
        word = request.POST.get('word')
    url = 'https://api.a3rt.recruit.co.jp/talk/v1/smalltalk'
    query = {
        'apikey':API_key,
        'query':word
    }
    r = requests.post(url, query)
    result = [r.json()]
    print(result)
    
    # return Response(result)
    return render(request, 'talkapp/talkAPI.html', {'word': word, 'result': result})

class TalkAPIViewSet(viewsets.ModelViewSet):
    serializer_class = TalkAPISerializer

class TalkModelViewSet(viewsets.ModelViewSet):
    queryset = TalkModel.objects.all()
    serializer_class = TalkModelSerializer

# def talkAPI(request):
#     print("talkAPI request")
#     API_key = env('API_KEY')
#     word = "ヌル"
#     if request.POST.get('word'):
#         word = request.POST.get('word')
#     url = 'https://api.a3rt.recruit.co.jp/talk/v1/smalltalk'
#     query = {
#         'apikey':API_key,
#         'query':word
#     }
#     r = requests.post(url, {'apikey':API_key,'query':word})
#     print(requests.get(url, params=query))
#     print("r")
#     print("response", r.json())
#     result = [r.json()]
    
#     return render(request, 'talkapp/talkAPI.html', {'word': word, 'result': result})