from django.db import models

class Customer(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    balance = models.FloatField(default=0)
    upi_pin = models.CharField(max_length=40)
class Transaction(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    t_type=models.CharField(max_length=20) #deposit/withdraw
    amount=models.FloatField()
    date=models.DateTimeField(auto_now_add=True)