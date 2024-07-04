from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Contract, Customer, Contact
from .forms import ContractForm, CustomerForm, UserForm, ContactForm

@login_required
def contract_list(request):
    contracts = Contract.objects.all()
    return render(request, 'contract_list.html', {'contracts': contracts})

@login_required
def contract_edit(request, pk):
    contract = get_object_or_404(Contract, pk=pk)
    if request.method == "POST":
        form = ContractForm(request.POST, instance=contract)
        if form.is_valid():
            form.save()
            return redirect('contract_list')
    else:
        form = ContractForm(instance=contract)
    return render(request, 'contract_edit.html', {'form': form})

@login_required
def contract_delete(request, pk):
    contract = get_object_or_404(Contract, pk=pk)
    contract.delete()
    return redirect('contract_list')

@login_required
def customer_create(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        customer_form = CustomerForm(request.POST)
        if user_form.is_valid() and customer_form.is_valid():
            user = user_form.save()
            customer = customer_form.save(commit=False)
            customer.user = user
            customer.save()
            return redirect('contract_list')
    else:
        user_form = UserForm()
        customer_form = CustomerForm()
    return render(request, 'customer_create.html', {
        'user_form': user_form,
        'customer_form': customer_form
    })

@login_required
def add_contract_to_cart(request):
    if request.method == "POST":
        form = ContractForm(request.POST)
        if form.is_valid():
            contract = form.save(commit=False)
            user = User.objects.create_user(
                username=form.cleaned_data['rut'],
                password='defaultpassword',
            )
            customer = Customer.objects.create(
                user=user,
                rut=form.cleaned_data['rut'],
                name=form.cleaned_data['name']
            )
            contract.customer = customer
            contract.save()
            return redirect('contract_list')
    else:
        form = ContractForm()
    return render(request, 'add_contract_to_cart.html', {'form': form})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'gestionviajes/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'gestionviajes/contact_success.html')

def index(request):
    context={}
    return render(request,'gestionviajes/index.html', context)