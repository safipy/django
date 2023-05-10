from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from phone_app.models import Phone, Reviews
from phone_app.forms import PhoneForm, ReviewForm
from django.views import generic


class PhoneListView(generic.ListView):
    template_name = "phone_list.html"
    queryset = Phone.objects.all()

    def get_queryset(self):
        return Phone.objects.all()


class PhoneDetailsView(generic.DetailView):
    template_name = "phone_details.html"

    def get_object(self, **kwargs):
        phone_id = self.kwargs.get("id")
        return get_object_or_404(Phone, id=phone_id)


class CreatePhoneView(generic.CreateView):
    template_name = "crud/create_phone.html"
    form_class = PhoneForm
    queryset = Phone.objects.all()
    success_url = "/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreatePhoneView, self).form_valid(form=form)


class DeleteOrUpdatePhoneListView(generic.ListView):
    template_name = "crud/delete_or_update_phone.html"
    queryset = Phone.objects.all()


class DeletePhoneView(generic.DeleteView):
    template_name = "crud/phone_delete.html"
    success_url = "/delete_or_update_phone_list/"

    def get_object(self, **kwargs):
        phone_id = self.kwargs.get("id")
        return get_object_or_404(Phone, id=phone_id)


class UpdatePhone(generic.UpdateView):
    template_name = "crud/phone_update.html"
    form_class = PhoneForm
    success_url = "/delete_or_update_phone_list/"

    def get_object(
        self,
    ):
        phone_id = self.kwargs.get("id")
        return get_object_or_404(Phone, id=phone_id)

    def form_valid(self, form):
        return super(UpdatePhone, self).form_valid(form=form)


# def phone_all_view(request):
#   phone_list = Phone.objects.all()
#  context = {
#     'phone_list': phone_list
# }
# eturn render(request, 'phone_list.html', context)

# def phone_details_view(request, id):
#     phone_details = get_object_or_404(Phone, id=id)
#     context = {
#         'phone_details': phone_details
#     }
#     return render(request,'phone_details.html', context)


# def create_phone_view(request):
#     method = request.method
#     if method == "POST":
#         form = PhoneForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("Смартфон успешно добавлен!")
#
#     else:
#         form = PhoneForm()
#     return render(request, 'crud/create_phone.html', {'form': form})


# def delete_phone_list_view(request):
#    delete_phone = Phone.objects.all()
#    return render(request, 'crud/delete_or_update_phone.html',
#                  {'del_phone': delete_phone})
#
#
# def phone_delete_detail_view(request, id):
#     phone_delete_id = get_object_or_404(Phone, id=id)
#     return render(request,'crud/phone_id_delete_or_update.html',
#                   {'phone_id_delete': phone_delete_id})
#
# def delete_phone_view(request, id):
#     phone_id = get_object_or_404(Phone, id=id)
#     phone_id.delete()
#     return HttpResponse("Смартфон успешно удален!")
#
# def update_phone_view(request, id):
#     phone_id = get_object_or_404(Phone, id=id)
#     if request.method == 'POST':
#         form = PhoneForm(instance=phone_id, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Смартфон успешно обновлён!')
#     else:
#         form = PhoneForm(instance=phone_id)
#
#     context = {
#         'form': form,
#         'phone_id': phone_id
#     }
#
#     return render(request, 'crud/phone_update.html', context)


class SearchView(generic.ListView):
    template_name = "phone_list.html"
    context_object_name = "phone"
    paginate_by = 5

    def get_queryset(self):
        return Phone.objects.filter(title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q")
        return context


class ReviewAddView(generic.CreateView):
    template_name = "reviews.html"
    form_class = ReviewForm
    queryset = Reviews.objects.all()
    success_url = "/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(ReviewAddView, self).form_valid(form=form)
