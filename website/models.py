from django.db import models
from django.conf import settings

# Create your models here.
class Member(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    # passwd =models.CharField(max_length=50)  
    age = models.CharField(max_length=100)
    skills=models.CharField(max_length=100) 
    Experience = models.CharField(max_length=100)
    CTC= models.CharField(max_length=100)
    resume=models.FileField(upload_to='documents/',null=True,default=None)

    # date = models.DateField()
    # photo = models.ImageFields


    def __str__(self):
         return self.fname + ' ' + self.lname

class Resume(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=50) 
    age = models.CharField(max_length=100)
    skills=models.CharField(max_length=100) 
    Experience = models.CharField(max_length=100)
    CTC= models.CharField(max_length=100)
    resume=models.FileField(upload_to='jobAspirents/',blank=True)