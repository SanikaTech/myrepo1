from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    message=models.TextField()

class Signup(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    date=models.DateField()
    phoneno=models.CharField(max_length=10)
  
class Feedback(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    phoneno=models.CharField(max_length=10)
    isSatisfied=models.BooleanField()
    suggestion=models.TextField()
class Order(models.Model):
    fname=models.CharField(max_length=25)
    lname=models.CharField(max_length=25)
    state=models.CharField(max_length=25)
    city=models.CharField(max_length=15)
    hometown=models.CharField(max_length=15)
    pincode=models.CharField(max_length=25)
    phone=models.CharField(max_length=10)
    email=models.EmailField()
    productname=models.CharField(max_length=20)
    price=models.CharField(max_length=20,default="0")
    address=models.TextField(default=None)



class Login(models.Model):
   username=models.CharField(max_length=12)
   password=models.EmailField()
    



