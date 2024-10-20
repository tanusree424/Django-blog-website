
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
   path('', index, name="home"),
   path('contact/', contact, name="contact"),
   path('about/', about, name="about") 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)