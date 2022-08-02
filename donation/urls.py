from django.urls import path

from donation.views.donationviews import DonationRequestView

urlpatterns = [
    path('request', DonationRequestView.as_view(), name='donation_request')
]
