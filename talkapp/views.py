import django_filters
from rest_framework import viewsets, filters

from .models import TalkModel
from .serializer import TalkModelSerializer

class TalkModelViewSet(viewsets.ModelViewSet):
    queryset = TalkModel.objects.all()
    serializer_class = TalkModelSerializer

