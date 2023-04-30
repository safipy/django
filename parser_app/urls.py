from django.urls import path
from . import views

urlpatterns = [
    path('start_parsing/', views.ParseFromView.as_view(), name='parser'),
    path('phone_parse_list/', views.ParsePhoneListView.as_view(), name='phone_list'),
]