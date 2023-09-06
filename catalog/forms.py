from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class VersionForm(StyleFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_active'].widget.attrs.update({'class': 'form-check-input'})

    class Meta:
        model = Version
        fields = '__all__'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data['name']
        forbidden_words = ['казино', 'биржа', 'наркотики', 'дешево', 'бесплатно', 'даром', 'обман', 'полиция', 'радар']
        for word in forbidden_words:
            if word in name.lower():
                raise forms.ValidationError('Название продукта содержит запрещенное слово!')
        return name

    def clean_description(self):
        description = self.cleaned_data['description']
        forbidden_words = ['казино', 'биржа', 'наркотики', 'дешево', 'бесплатно', 'даром', 'обман', 'полиция', 'радар']
        for word in forbidden_words:
            if word in description.lower():
                raise forms.ValidationError('Описание продукта содержит запрещенное слово!')
        return description
