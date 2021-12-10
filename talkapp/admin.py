from django.contrib import admin

from talkapp.models import TalkModel, UserModel, UserLike

# Register your models here.

@admin.register(TalkModel)
class TalkModel(admin.ModelAdmin):
    pass

admin.site.register(UserModel)
admin.site.register(UserLike)