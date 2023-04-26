from django.urls import path
from phone_app.views import phone_all_view, phone_details_view, create_phone_view, delete_phone_list_view,\
    phone_delete_detail_view, delete_phone_view, update_phone_view

urlpatterns = [
    path('phone_list/', phone_all_view, name='phone_list'),
    path('phone_list/<int:id>/', phone_details_view, name='phone_details'),
    path('add-phone/', create_phone_view, name='create_phone'),
    path('delete_phone_list/', delete_phone_list_view, name='delete_phone_list'),
    path('delete_phone_list/<int:id>/', phone_delete_detail_view, name='delete_phone_id'),
    path('delete_phone_list/<int:id>/delete/', delete_phone_view, name='delete_phone_id'),
    path('update_phone_list/<int:id>/update/', update_phone_view, name='update_phone_id'),
]