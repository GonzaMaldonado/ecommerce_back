from django.urls import path
from rest_framework_simplejwt.views import (
      TokenRefreshView,
      TokenVerifyView
  )
from .views import LoginView, register

urlpatterns = [
    path('register/', register),
    path('login/', LoginView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),
]