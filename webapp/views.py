from django.shortcuts import render, redirect
from .models import *
from django.forms import ModelForm
from .forms import CustomerForm


def HomePage(request):
    return render(request, 'pages/homepage.html')

def Home(request):
    customer  = Customer.objects.all()
    payment = Payment.objects.all()
    returns = Return.objects.all ()
    
    total_customer = customer.count()
    total_payment = payment.count()

    context = {
        'customer':customer,

    }
    return render(request, 'pages/home.html', {'customer':customer})

def profilePage(request, pk):
    customer  = Customer.objects.get(id=pk)
    payment = customer.payment_set.all()
    
    context = {
        'customer':customer,
    }

    return render(request,'pages/profile.html', context)

def createCustomer(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home')

    context = {'form': form}
    return render(request, 'pages/createCustomer.html', context)

def updateCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)
    
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('Home')
    context = {'form':form}
    return render(request, 'pages/createCustomer.html', context)

def deleteCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('Home')
    context = {'customer':customer}
    return render(request, 'pages/createCustomer.html', context)

def index(request):
    return render(request, 'pages/index.html')
def NavBar(request):
    return render(request, 'pages/navbar.html')
def Footer(request):
    return render(request, 'pages/footer.html')  
def Audio(request):
    return render(request, 'pages/audio.html')
def Cart(request):
    return render(request, 'pages/cart.html') 
