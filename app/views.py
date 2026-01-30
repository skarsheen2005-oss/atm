from django.shortcuts import render,redirect
from .models import Customer,Transaction

#register
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        upi_pin = request.POST['upi_pin']
        if Customer.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})
        Customer.objects.create(username=username, password=password,upi_pin=upi_pin)
        return redirect('login')
    return render(request, 'register.html')

#info
# def info(request):
#     customer=Customer.objects.all()
#     return render(request,'info.html',{'customer':customer})

#login
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            customer= Customer.objects.get(username=username, password=password)
            return redirect('dashboard',username=customer.username)
        except Customer.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid credentials'})  
    return render(request,'login.html')

#dashboard
def dashboard(request,username):
    customer=Customer.objects.get(username=username)
    transactions=Transaction.objects.filter(customer=customer).order_by('-date')
    return render(request,'dashboard.html',{
        'customer':customer,
        'transactions':transactions
         })

#deposit
def deposit(request,username):
    customer=Customer.objects.get(username=username)
    if request.method=='POST':
        amount=int(request.POST['amount'])
        upi_pin=request.POST['upi_pin']
        if upi_pin==customer.upi_pin:
            customer.balance+=amount
            customer.save()
            Transaction.objects.create(customer=customer, t_type="DEPOSIT", amount=amount)
            return redirect('dashboard',username=customer.username)
        else:
            return render(request,'deposit.html',{'username':username,'error':'Invalid UPI PIN'})
    return render(request,'deposit.html')

#withdraw
def withdraw(request,username):
    customer=Customer.objects.get(username=username)
    if request.method=='POST':
        amount=int(request.POST['amount'])
        upi_pin=request.POST['upi_pin']
        if upi_pin==customer.upi_pin:
            if amount<=customer.balance:
                customer.balance-=amount
                customer.save()
                Transaction.objects.create(customer=customer, t_type="withdraw", amount=amount)
                return redirect('dashboard',username=customer.username)
            else:
                return render(request,'withdraw.html',{'username':username,'error':'Insufficient balance'})
    return render(request,'withdraw.html')

#change_upi_pin
def change_upi_pin(request,username):
    customer=Customer.objects.get(username=username)
    if request.method=='POST':
        old_upi_pin=request.POST['old_pin']
        new_upi_pin=request.POST['new_pin']
        if old_upi_pin==customer.upi_pin:
            customer.upi_pin=new_upi_pin
            customer.save()
            return redirect('dashboard',username=customer.username)
        else:
            return render(request,'change_upi_pin.html',{'username':username,'error':'Invalid old UPI PIN'})
    return render(request,'change_upi_pin.html')




