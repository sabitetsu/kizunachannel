from django.contrib import admin
from django.urls import path

from rest_framework import routers, views
from . import views
from talkapp.views import TalkModelViewSet, talkAPI



router = routers.DefaultRouter()
router.register(r'talkmodel', TalkModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('talkAPI/', views.talkAPI, name='talkAPI'),
]

urlpatterns += router.urls