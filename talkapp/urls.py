from django.contrib import admin
from django.urls import path

from rest_framework import routers, views
from . import views
from talkapp.views import TalkModelViewSet, talkAPI, wordRegist



router = routers.DefaultRouter()
router.register(r'talkmodel', TalkModelViewSet)

urlpatterns = [
    path('talkAPI/', views.talkAPI, name='talkAPI'),
    path('wordRegist/',views.wordRegist, name='wordRegist'),
]

urlpatterns += router.urls