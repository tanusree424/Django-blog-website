from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from home.models import UserProfile
from tinymce.models import HTMLField
from home.models import CustomUser
# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000)
    content = HTMLField() 
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    slug = models.CharField(max_length=100, default="")
    image = models.ImageField(upload_to='user/', default=0)
    view = models.IntegerField(default=0)
    timestamps = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return f"{self.title} - {self.author.username} "
    class Meta:
        permissions = [
            ("can_view_post", "Can view post"),
            ("can_edit_own_post", "Can edit own post"),
        ]
class PostView(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'ip_address') 
class Comment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,related_name='replies')  # Allows replies
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, null=True)  # Fixed the typo
    timestamps = models.DateTimeField(default=now)

    def __str__(self):
        return f"Commented by - {self.user.username}"
  
    


 


   

