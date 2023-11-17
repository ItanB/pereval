from django.urls import path
from .import api
from .views import PerevalAddedViewSet, UsersViewSet, SubmitDetailData, SubmitData
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'pereval', PerevalAddedViewSet)
router.register(r'users', UsersViewSet)
router.register(r'SubmitData', PerevalAddedViewSet, basename='SubmitData')
router.register(r'SubmitDetailData', PerevalAddedViewSet, basename='SubmitDetailData')
router.register(r'SubmitData', UsersViewSet, basename='SubmitData')
router.register(r'SubmitDetailData', UsersViewSet, basename='SubmitDetailData')

urlpatterns = [
    path('api/v1/submitData/', SubmitData.as_view(), name='submitData'),
    path('api/v1/submitData/<int:pk>/', SubmitDetailData.as_view(), name='submitDetailData'),
    path('api/v1/submitData/?users__email=email/', SubmitData.as_view(), name='email'),
]
urlpatterns.extend(router.urls)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
