from django.urls import path
from . import api
from .views import PerevalAddedViewSet, UsersViewSet
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'pereval', PerevalAddedViewSet)
router.register(r'users', UsersViewSet)

urlpatterns = [
    path('users/', api.UsersListApiView.as_view(), name='api_users'),
    path('pereval/', api.PerevalAddedListAPIView.as_view(), name='api_pereval'),

]
urlpatterns.extend(router.urls)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
