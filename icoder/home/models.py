from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=2000)
    email = models.CharField(max_length=2000)
    description = models.TextField(max_length=50000)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"Message from : {self.name} - {self.email}"