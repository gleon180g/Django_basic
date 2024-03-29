from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images')
    designation= models.CharField(max_length=100)
    emial_address=models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=12,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at= models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.first_name