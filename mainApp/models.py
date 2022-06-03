from django.db import models

# Create your models here.
class mail(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    subject=models.CharField(max_length=100)
    message=models.CharField(max_length=500)
    def __str__(self):
        return self.name
