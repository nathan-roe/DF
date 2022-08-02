from django.urls import path

from users.views.recipientviews import RecipientSignUpView

urlpatterns = [
    path('recipient-signup', RecipientSignUpView.as_view(), name='recipient_signup'),
]
