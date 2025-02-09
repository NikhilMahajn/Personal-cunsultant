from django.db import models

# Create your models here.
class Message(models.Model):
    name=models.CharField(max_length=30)
    eMail=models.EmailField(max_length=50)
    subject=models.CharField(max_length=200)
    userMessage=models.CharField(max_length=1000)
    
	