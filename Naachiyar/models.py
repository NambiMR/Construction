from django.db import models

# Create your models here.
class user(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)

class admin(models.Model):
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
        age=models.IntegerField()
        email=models.EmailField(max_length=50)
        mobile=models.CharField(max_length=10)
        role=models.CharField(max_length=50)
        experience=models.CharField(max_length=10)
        city=models.CharField(max_length=10)
        pincode=models.IntegerField()
        date=models.CharField(max_length=50)
        def __str__(self):
            return self.name
    

        
class Feedback(models.Model):
        Name=models.CharField(max_length=50)
        Email=models.EmailField(max_length=50)
        Age=models.IntegerField()
        Phone=models.CharField(max_length=10)
        Message=models.CharField(max_length=250)
        Rate=models.CharField(max_length=50, null=True)
        def __str__(self):
            return self.Name
    
class Worker(models.Model):
        name=models.CharField(max_length=50)
        age=models.IntegerField()
        contact=models.CharField(max_length=10)
        designation=models.CharField(max_length=250)
        def __str__(self):
          return self.name
        
class Project(models.Model):
        project_name=models.CharField(max_length=50)
        client_name=models.CharField(max_length=50)
        mobile=models.CharField(max_length=10)
        location=models.CharField(max_length=250)
        budget=models.CharField(max_length=50)
        s_date = models.DateField(default=None, blank=True, null=True)
        status = models.CharField(max_length=50)
        e_date = models.DateField(default=None, blank=True, null=True)
        def __str__(self):
          return self.project_name
        

        
""" class Employee(models.Model):
    name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.name
    
class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('present', 'Present'), ('absent', 'Absent')])
    
    def __str__(self):
        return f"{self.employee.name} - {self.date}" """

