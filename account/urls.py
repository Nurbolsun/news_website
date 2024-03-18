from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
    RegistrationView, LoginView, UserProfileView,
    PasswordResetRequestView, OTPVerificationView,
    CreateNewPasswordView, LogoutView, DeleteAccountView,
    ChangePasswordView, SubscribeToNewsletterView,
    UnsubscribeFromNewsletterView
)


urlpatterns = [
    path('auth/register/', RegistrationView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('auth/delete-account/', DeleteAccountView.as_view(), name='delete-account'),
    path('user-profile/', UserProfileView.as_view(), name='user-profile'),
    path('user-profile/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('auth/password-reset/', PasswordResetRequestView.as_view(), name='password-reset-request'),
    path('auth/otp-verification/', OTPVerificationView.as_view(), name='otp-verification'),
    path('auth/set-new-password/', CreateNewPasswordView.as_view(), name='set-new-password'),
    path('subscribe/', SubscribeToNewsletterView.as_view(), name='subscribe-to-newsletter'),
    path('unsubscribe/', UnsubscribeFromNewsletterView.as_view(), name='unsubscribe-from-newsletter'),

    # path('token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]
