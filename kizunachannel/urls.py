from django.contrib import admin
from django.urls import path, include
from . import views
from kizunachannel.views import index, fav

urlpatterns = [
    path('', views.index, name='index'),
    #path('favicon.ico/', views.fav, name='fav'),
    path('admin/', admin.site.urls),
    path('talk/', include('talkapp.urls')),
    path('web/', include('webpage.urls')),
]
