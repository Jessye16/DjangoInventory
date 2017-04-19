from django import forms
from inventory.models import Product

class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product 
        fields = ('name', 'brand', 'type', 'gender', 'description', 'quantity', 'modified_by', 'modified_at')