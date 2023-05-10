from django.urls import path
from . import views

urlpatterns = [
    path("cloth_list/", views.ProductListView.as_view(), name="product_list"),
    path(
        "cloth_list/<int:id>/", views.ProductDetailView.as_view(), name="product_detail"
    ),
    path("add-order/", views.OrderCreateView.as_view(), name="add_order"),
    path("women/", views.ClothWomenListView.as_view(), name="women"),
    path("man/", views.ClothManListView.as_view(), name="man"),
    path("shoes/", views.ClothShoesListView.as_view(), name="shoes"),
    path("accessories/", views.ClothAccessoriesListView.as_view(), name="accessories"),
]
