from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('contracts/', views.contract_list, name='contract_list'),
    path('contracts/<int:pk>/edit/', views.contract_edit, name='contract_edit'),
    path('contracts/<int:pk>/delete/', views.contract_delete, name='contract_delete'),
    path('customers/create/', views.customer_create, name='customer_create'),
    path('contracts/add/', views.add_contract_to_cart, name='add_contract_to_cart'),
    path('contacts/', views.contact, name='contact'),
    path('contacts/success/', views.contact_success, name='contact_success'),
    path('usuarios/', views.crud_usuarios, name='crud_usuarios'),
    path('index/', views.index, name='index'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]
