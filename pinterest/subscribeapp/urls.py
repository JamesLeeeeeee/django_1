from django.urls import path

from .views import SubscriptionView

app_name = "subscribeapp"




urlpatterns = [
    path('subscribe/', SubscriptionView.as_view(), name='subscribe')

]