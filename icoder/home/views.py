from django.shortcuts import render
from .models import Contact

# Create your views here.
def index(request):
    return render(request,"home/home.html")
def contact(request):
    if request.method =="POST":
        name = request.POST['name']
        email = request.POST['email']
        issue = request.POST['issue']
        contact = Contact(name = name , email = email, description=issue)
        contact.save()
    
    return render(request,"home/contact.html")
def about(request):
    return render(request,"home/about.html")