from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.name

class College(models.Model):
    name = models.CharField(max_length=128)
    location = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.name

class Car(models.Model):
    name=models.CharField(max_length=128)
    price=models.CharField(max_length=128)
    def __str__(self):
        return self.name

