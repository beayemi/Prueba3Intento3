from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Contract, Customer, Contact, Cart
from .forms import ContractForm

@login_required
def add_contract_to_cart(request):
    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            # Guardar el contrato en la base de datos
            contract = form.save(commit=False)
            
            # Obtener o crear el cliente asociado al usuario actual
            customer, created = Customer.objects.get_or_create(user=request.user)
            contract.customer = customer
            contract.save()
            
            # Agregar el contrato al carrito del usuario
            cart, created = Cart.objects.get_or_create(user=request.user)
            cart.contracts.add(contract)
            cart.save()

            return redirect('carrito')  # Redirige al carrito después de agregar
    else:
        form = ContractForm()

@login_required
def carrito(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = cart.contracts.all()
    total = sum(item.price for item in items)

    return render(request, 'carrito.html', {'items': items, 'total': total})

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
    context = {}
    return render(request, 'gestionviajes/index.html', context)

def crud_usuarios(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'gestionviajes/usuarios.html', context)

def procesar_pago(request):
    # Lógica para procesar el pago
    return render(request, 'gestionviajes/procesar_pago.html')