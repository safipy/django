from django import forms
from . import models, parser

class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('smartphone.kg', 'smartphone.kg'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = [
            'media_type'
        ]

    def parser_data(self):
        if self.data['media_type'] == 'smartphone.kg':
           phone_parser = parser.parser()
           for i in phone_parser:
               models.Smartphone.objects.create(**i)