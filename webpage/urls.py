from django.urls import path
from .views import jsonview

urlpatterns = [
    path('json/', jsonview, name='json'),
]
