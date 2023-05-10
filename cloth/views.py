from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, CreateView
from . import models, forms


class ProductListView(ListView):
    queryset = models.ProductCL.objects.filter().order_by("-id")
    template_name = "cloth/cloth_list.html"

    def get_queryset(self):
        return models.ProductCL.objects.filter().order_by("-id")


class ClothWomenListView(ListView):
    queryset = models.ProductCL.objects.filter(tag__name="women")
    template_name = "cloth/cloth_women_list.html"

    def get_queryset(self):
        return models.ProductCL.objects.filter(tag__name="women")


class ClothManListView(ListView):
    queryset = models.ProductCL.objects.filter(tag__name="man")
    template_name = "cloth/cloth_man_list.html"

    def get_queryset(self):
        return models.ProductCL.objects.filter(tag__name="man")


class ClothShoesListView(ListView):
    queryset = models.ProductCL.objects.filter(tag__name="shoes")
    template_name = "cloth/shoes_list.html"

    def get_queryset(self):
        return models.ProductCL.objects.filter(tag__name="shoes")


class ClothAccessoriesListView(ListView):
    queryset = models.ProductCL.objects.filter(tag__name="accessories")
    template_name = "cloth/accessories_list.html"

    def get_queryset(self):
        return models.ProductCL.objects.filter(tag__name="accessories")


class ProductDetailView(DetailView):
    template_name = "cloth/product_detail.html"

    def get_object(self, **kwargs):
        product_id = self.kwargs.get("id")
        return get_object_or_404(models.ProductCL, id=product_id)


class OrderCreateView(CreateView):
    template_name = "add_order.html"
    form_class = forms.OrderForm
    success_url = "/cloth_list/"
    queryset = models.OrderCL.objects.all()

    def form_valid(self, form):
        return super(OrderCreateView, self).form_valid(form=form)
