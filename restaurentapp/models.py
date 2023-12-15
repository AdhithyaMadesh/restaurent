from django.db import models
# from django-phone-field import PhoneField
# from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class submit(models.Model):
    Name=models.CharField(max_length=300)
    People=models.CharField(max_length=100)
    Mobile =models.CharField(max_length=100)
    # Mobile=models.CharField(max_length=100)
    Time=models.TimeField()
    Date=models.DateField()
    Mail=models.EmailField()
    