from django.urls import path

from df_auth.views.userauthenticationviews import EmailVerificationView


urlpatterns = [
    path('verify-email', EmailVerificationView.as_view(), name='email_verification')
]
