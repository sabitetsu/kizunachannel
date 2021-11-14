from django.contrib import admin
from django.urls import path

from rest_framework import routers

from talkapp.views import TalkModelViewSet

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

router = routers.DefaultRouter()
router.register(r'talkmodel', TalkModelViewSet)
urlpatterns = router.urls