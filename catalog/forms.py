from django import forms
from django.core.exceptions import ValidationError
from .models import Product

FORBIDDEN_WORDS = [
    'казино', 'криптовалюта', 'крипта', 'биржа',
    'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'price')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        name = self.cleaned_data.get('name', '')
        for word in FORBIDDEN_WORDS:
            if word in name.lower():
                raise ValidationError(f'Использование слова "{word}" запрещено.')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        for word in FORBIDDEN_WORDS:
            if word in description.lower():
                raise ValidationError(f'Использование слова "{word}" запрещено.')
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise ValidationError('Цена продукта не может быть отрицательной.')
        return price

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            # Проверка размера (5 МБ)
            max_size = 5 * 1024 * 1024
            if image.size > max_size:
                raise ValidationError('Размер файла не должен превышать 5 МБ.')

            # Проверка формата (JPEG или PNG)
            valid_extensions = ['jpg', 'jpeg', 'png']
            ext = image.name.split('.')[-1].lower()
            if ext not in valid_extensions:
                raise ValidationError('Допустимые форматы изображений: JPEG или PNG.')

        return image
