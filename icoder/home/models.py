from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils.timezone import now
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000)
    email = models.TextField(max_length=10000)
    description = models.CharField(max_length=5000)
    phone = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name}"
class UserProfile(models.Model):  # Corrected the class name
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_img = models.ImageField(upload_to='user/', default='user/user.png', blank=True)# Field for user's image
    school = models.CharField(max_length=200)
    college = models.CharField(max_length=200, default="")
    phone = models.CharField(max_length=200, default="")
    address = models.TextField(default="")
    marital_status = models.CharField(max_length=200, default="")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="")

    def __str__(self):
        return f"{self.user.username}"



class CustomUser(AbstractUser):
    # Add any additional fields here if necessary
    role = models.CharField(max_length=50, blank=True, null=True)
    photo = models.ImageField(upload_to='authors/', null=True, blank=True)
    education = models.TextField(null=True, blank=True)
    # Define custom related_name for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Custom related name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions_set',  # Custom related name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

