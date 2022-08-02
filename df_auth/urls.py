from django.urls import path

from df_auth.views.userauthenticationviews import EmailVerificationView, ExpiringAuthTokenView


urlpatterns = [
    path('verify-email', EmailVerificationView.as_view(), name='email_verification'),
    path('login', ExpiringAuthTokenView.as_view(), name='login')
]
