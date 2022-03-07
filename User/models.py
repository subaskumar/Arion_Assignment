from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your models here.

class Destinations(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    
    def __str__(self):
        return self.city
  
class Profile(modes.Model):
    gender_choice = (
        ('Male', 'Male')
        ('Female', 'Female')
        ('Others', 'Others')

    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50)
    DOB = models.DateField()
    gender = models.CharField(max_length=50, choices = gender_choice, default='Male')
    phone = models.CharField(max_length=50)
    
class UserAddress(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    address3 = models.CharField(max_length=50)
    pincode = models.CharField(max_length=50)
 