from django.shortcuts import render
from inventory.models import Product
from django.views.generic import CreateView
from django.views.generic import ListView
from inventory.forms import ProductCreateForm


# Create your views here.
class ProductListView(ListView):
    model = Product
    context_object_name="products"
    template_name="inventory/product-list.html" 
    paginate_by=None #

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductCreateForm
    template_name = "inventory/product-create.html"

    def get_initial(self):
        return {'modified_by': self.request.user.member}