from django.forms import ModelForm
from main.models import Product
from django import forms
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "category", "thumbnail", "is_featured"]

        def clean_name(self):
            name = self.cleaned_data["name"]
            return strip_tags(name)

        def clean_content(self):
            description = self.cleaned_data["description"]
            return strip_tags(description)


