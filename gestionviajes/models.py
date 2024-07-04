from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=12, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Contract(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    destination = models.CharField(max_length=100)
    departure_date = models.DateField()
    return_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.name} - {self.destination}"
