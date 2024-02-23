from django.db import models

# Create your models here.
class user(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    subject=models.TextField()
    def __str__(self):
        return self.name
    
class Quote(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=10)
    description=models.CharField(max_length=250)
    budget=models.CharField(max_length=10)
    s_date=models.CharField(max_length=10)
    e_date=models.CharField(max_length=10)
    location=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Job(models.Model):
        name=models.CharField(max_length=50)
        age=models.IntegerField(max_length=50)
        email=models.EmailField(max_length=50)
        mobile=models.CharField(max_length=10)
        role=models.CharField(max_length=50)
        experience=models.CharField(max_length=10)
        city=models.CharField(max_length=10)
        pincode=models.IntegerField(max_length=10)
        date=models.CharField(max_length=50)
        def __str__(self):
            return self.name
    
class Worker(models.Model):
        name=models.CharField(max_length=50)
        age=models.IntegerField(max_length=50)
        contact=models.CharField(max_length=10)
        designation=models.CharField(max_length=250)
        def __str__(self):
          return self.name
        
