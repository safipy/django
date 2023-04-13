from django.urls import path
from phone_app.views import phone_all_view, phone_details_view

urlpatterns = [
    path('phone_list/', phone_all_view, name='phone_list'),
    path('phone_list/<int:id>', phone_details_view, name='phone_details')
]