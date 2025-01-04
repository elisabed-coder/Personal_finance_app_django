from django.urls import path
from .views import RegistrationView, LoginView, ForgotPasswordView,  ResetPasswordView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("register/", RegistrationView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("forgotPassword/", ForgotPasswordView.as_view(), name="forgotPassword"),
    path("resetPassword/", ResetPasswordView.as_view(), name="resetPassword"),

]