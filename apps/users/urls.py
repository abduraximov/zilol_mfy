from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.users.api_endpoints import user

urlpatterns = [
    path(
        "UserRegistration/",
        user.UserRegistrationAPIView.as_view(),
        name="UserRegistration",
    ),
    path("Login/", TokenObtainPairView.as_view(), name="Login"),
    path("TokenRefresh/", TokenRefreshView.as_view(), name="TokenRefresh"),
]
