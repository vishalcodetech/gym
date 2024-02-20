from django.db import models

# Create your models here. 
class Contact(models.Model): 
    name = models.CharField(max_length = 100) 
    email = models.EmailField() 
    subject= models.IntegerField() 
    message=models.CharField(max_length=400) 
 
    def __str__(self): 
        return self.email
    
class Service(models.Model):
       service_icon=models.CharField(max_length=200)
       service_title=models.CharField(max_length=200)
       service_desc=models.TextField()

       def __str__(self):
           return self.service_title
