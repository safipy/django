from django.shortcuts import render, get_object_or_404
from phone_app.models import Phone

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
