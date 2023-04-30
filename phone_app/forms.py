from django import forms
from . import models


class PhoneForm(forms.ModelForm):
    class Meta:
        model = models.Phone
        fields = "__all__"

class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Reviews
        fields = '__all__'