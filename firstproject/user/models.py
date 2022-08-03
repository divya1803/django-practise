from django.db import models

class Details(models.Model):
    name=models.CharField(max_length=68)
    email=models.EmailField(max_length=128)
    phone_number=models.CharField(max_length=128)
    def __str__(self):
        return self.email


