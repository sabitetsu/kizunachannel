from django.contrib import admin

from talkapp.models import TalkModel

# Register your models here.

@admin.register(TalkModel)
class TalkModel(admin.ModelAdmin):
    pass