from django.urls import path
from .views import RegistrationAPIView, LoginAPIView, SendPasswordResetOtpView, SetNewPasswordView


urlpatterns = [
    path('register', RegistrationAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('password-reset-otp', SendPasswordResetOtpView.as_view()),
    path('reset-password', SetNewPasswordView.as_view())
]
