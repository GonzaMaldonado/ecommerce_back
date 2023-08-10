from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
      TokenRefreshView,
      TokenVerifyView
  )
from .views import LoginView, register, UserViewSet

router = DefaultRouter()
router.register(r'', UserViewSet, basename='users')


urlpatterns = [
    path('register/', register),
    path('login/', LoginView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('', include(router.urls))
]