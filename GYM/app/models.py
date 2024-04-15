from django.db import models



class AdminDataBase(models.Model):
    FirstName=models.CharField(max_length=50)
    lastName=models.CharField(max_length=50)
    Email=models.EmailField()
    Contact=models.IntegerField()
    Password=models.CharField(max_length=10)
    def __str__(self):
        return self.FirstName + " " +self.lastName
    
class Customer(models.Model):
    name=models.CharField(max_length=40)
    lname=models.CharField(max_length=40)
    email=models.EmailField(max_length=40)
    age=models.IntegerField()
    identity=models.IntegerField()
    image=models.FileField(upload_to='')
    
