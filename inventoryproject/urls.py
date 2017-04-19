"""inventoryproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from inventory.views import ProductCreateView
from inventory.views import ProductListView
from inventory.views import ProductDetailView
from inventory.views import ProductUpdateView
from inventory.views import ProductDeleteView
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^accounts/profile/$', TemplateView.as_view(template_name='test.html'), name='user_profile'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^jjj', ProductListView.as_view(), name='product-list'),
    url(r'create/', ProductCreateView.as_view(), name='create-product'),
    url(r'^(?P<pk>\d+)/$', ProductDetailView.as_view(), name='product-detail'),
    url(r'^(?P<pk>\d+)/update/', ProductUpdateView.as_view(), name='product-update'),
    url(r'^(?P<pk>\d+)/delete/', ProductDeleteView.as_view(), name='product-delete'),
    url(r'^$', 'inventory.views.login_redirection', name='login_redirection')
]
