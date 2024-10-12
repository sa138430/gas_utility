from django.urls import path
from . import views

urlpatterns = [
    path('create-request/', views.create_request, name='create_request'),
    path('track-request/', views.track_request, name='track_request'),
    path('account-details/', views.account_details, name='account_details'),
]