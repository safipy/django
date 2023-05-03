from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

USER_TYPE = [
    ('Админ', 'Админ'),
    ('ВИП Клиент', 'ВИП Клиент'),
    ('Клиент', 'Клиент')
]
GENDER = [
    ('М', 'М'),
    ('Ж', 'Ж')
]

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.IntegerField(required=True)
    age = forms.IntegerField(required=True)
    user_type = forms.ChoiceField(choices=USER_TYPE, required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)

    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'age',
            'user_type',
            'gender'
        )
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user















