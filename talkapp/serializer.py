from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import TalkModel

class TalkModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TalkModel
        fields = ('inputWord','outputWord')

class TalkAPISerializer(serializers.ModelSerializer):
    class Meta:
        fields = ()