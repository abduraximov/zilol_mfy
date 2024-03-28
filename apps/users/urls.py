from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.users.api_endpoints import user

urlpatterns = [
    path("UserRegistration/", user.UserRegistrationAPIView.as_view(), name="UserRegistration"),
    path("Login/", TokenObtainPairView.as_view(), name="Login"),
]
