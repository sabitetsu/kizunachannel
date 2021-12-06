from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('talk/', include('talkapp.urls')),
    path('web/', include('webpage.urls')),
]
