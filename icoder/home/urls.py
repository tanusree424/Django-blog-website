
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
   path('', index, name="home"),
   path('contact/', contact, name="contact"),
   path('about/', about_view, name="about"),
   path('search/', search, name="search"), 
   path('signup/',handleSignup, name="signup"), 
   path('login/', handlelogin, name="login"), 
   path('logout/',handlelogout, name="handlelogout"), 
   
   path('profile/',profile, name="profile"), 
   path('profile_add_edit/',profile_add_edit, name="profile_add_edit"), 
   path('about/<int:author_id>/', author_detail, name='author_detail'),
   path('update_profile/<int:profile_id>/',update_profile , name='updateprofile'),
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)