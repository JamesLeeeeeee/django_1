from django.urls import path
from django.views.generic import TemplateView

template_name = 'articleapp'

urlpatterns = [
    path('list/', TemplateView.as_view(template_name='articleapp/list.html'), name='list')
]