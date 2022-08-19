from django.urls import path

from .views import SubscriptionView, SubscriptionListView

app_name = "subscribeapp"




urlpatterns = [
    path('subscribe/', SubscriptionView.as_view(), name='subscribe'),
    path('list/', SubscriptionListView.as_view(), name='list'),

]