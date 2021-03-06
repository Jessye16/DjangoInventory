from django.shortcuts import render
from inventory.models import Product
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from inventory.forms import ProductCreateForm
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
class RegisterCreateView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/register.html"
    success_url='/'

class ProductListView(ListView):
    model = Product
    context_object_name="products"
    template_name="inventory/product-list.html" 
    paginate_by=None 

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductCreateForm
    template_name = "inventory/product-create.html"

class ProductDetailView(DetailView):
    model = Product
    context_object_name = "details"
    template_name = "inventory/product-detail.html"

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductCreateForm
    template_name = "inventory/product-update.html"

class ProductDeleteView(DeleteView):
    model = Product
    form_class = ProductCreateForm
    template_name = "inventory/product-delete.html"
    success_url = '/list'

    def get_initial(self):
        return {'modified_by': self.request.user.member}

def login_redirection(request):
    return redirect('login')