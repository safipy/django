from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from phone_app.models import Phone
from phone_app.forms import PhoneForm
def phone_all_view(request):
    phone_list = Phone.objects.all()
    context = {
        'phone_list': phone_list
    }
    return render(request, 'phone_list.html', context)


def phone_details_view(request, id):
    phone_details = get_object_or_404(Phone, id=id)
    context = {
        'phone_details': phone_details
    }
    return render(request,'phone_details.html', context)

def create_phone_view(request):
    method = request.method
    if method == "POST":
        form = PhoneForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Смартфон успешно добавлен!")

    else:
        form = PhoneForm()
    return render(request, 'crud/create_phone.html', {'form': form})



def delete_phone_list_view(request):
   delete_phone = Phone.objects.all()
   return render(request, 'crud/delete_or_update_phone.html',
                 {'del_phone': delete_phone})


def phone_delete_detail_view(request, id):
    phone_delete_id = get_object_or_404(Phone, id=id)
    return render(request,'crud/phone_id_delete_or_update.html',
                  {'phone_id_delete': phone_delete_id})

def delete_phone_view(request, id):
    phone_id = get_object_or_404(Phone, id=id)
    phone_id.delete()
    return HttpResponse("Смартфон успешно удален!")

def update_phone_view(request, id):
    phone_id = get_object_or_404(Phone, id=id)
    if request.method == 'POST':
        form = PhoneForm(instance=phone_id, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Смартфон успешно обновлён!')
    else:
        form = PhoneForm(instance=phone_id)

    context = {
        'form': form,
        'phone_id': phone_id
    }

    return render(request, 'crud/phone_update.html', context)














