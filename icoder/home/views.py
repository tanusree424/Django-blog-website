from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import Contact,UserProfile,CustomUser
from django.contrib import messages
from blog.models import Post
from django.db.models import Count
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from blog.models import Post

def index(request):
    # Fetch the top 3 posts based on the highest view count
    popular_posts = Post.objects.order_by('-view')[:3]  # Orders by view count in descending order

    # Pass the popular posts to the template
    context = {
        'popular_posts': popular_posts
    }
    return render(request, "home/home.html", context)
def contact(request):
    if request.method =="POST":
        name = request.POST['name']
        email = request.POST['email']
        issue = request.POST['issue']
        phone  = request.POST['phone']
        print(phone)
        if len(name) < 5 or len(email)<5 or len(phone) == 10 or len(issue)<4:
            messages.error(request,"Please fill all the fields correctly")
     
        else:
            contact = Contact(name = name , email = email, description=issue ,phone=phone)
            contact.save()
        
            messages.success(request, "Message sent")
    
    return render(request,"home/contact.html")
def about_view(request):
    # authors = CustomUser.objects.all()
    authors =UserProfile.objects.filter(user__in=User.objects.filter(posts__isnull=False)).select_related('user').distinct()
    return render(request, 'home/about.html', {'authors': authors})
def search(request):
    data ={}
    if request.method == "GET":
        search_data = request.GET.get('search')
        if len(search_data) > 78:
         posts = Post.objects.none()
         
        else:
            if search_data:
                posts = Post.objects.filter(Q(title__icontains=search_data) | Q(content__icontains=search_data) | Q(author__icontains=search_data))
                data = {"posts":posts,"search_data":search_data}
            else:
                messages.warning(request, "No search results found. Please refine your query.")


    return render(request,"home/search.html",data)
def handleSignup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        pass1 = request.POST['password']
       
        confirm_password = request.POST['confirm_password']
        if len(username) >30:
            messages.error(request,"Username mustbe in 10 characters")
            return redirect('home')
        elif pass1 != confirm_password:
            messages.error(request,"Password do not match")
            return redirect('home')
        elif not str(username).isalnum():
            messages.error(request,"Username must be in alphanumeric")
            return redirect('home')
        else:
            myuser = User.objects.create_user(username,email,pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
          
    

            messages.success(request,"Your iCoder account has been successfully created")
            return redirect('home')

    else:
        return HttpResponse('''<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

    <title> 
                            Not- Found
    </title>
    </head>
                            <body class="h-100 vh-100 d-flex justify-content-center align-items-center">
                            
                            <h1> 404- Not Found</h1>
                              <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

                            </body>
                            </html>
                            ''')
def handlelogin(request):
    if request.method =="POST":
        loginusername = request.POST.get('username')
        loginpassword = request.POST.get('password')
        user = authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            login(request,user)
            messages.success(request,f'''{request.user} Successfully login''')
            return redirect('home')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('home') 
    return HttpResponse( 
        '''<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

    <title> 
                            Not- Found
    </title>
    </head>
                            <body class="h-100 vh-100 d-flex justify-content-center align-items-center">
                            
                            <h1> 404- Not Found</h1>
                              <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

                            </body>
                            </html>
                            ''')


@login_required
def handlelogout(request):
    logout(request)
    messages.success(request," You are successfully logged out")
    return redirect('home')
@login_required
def profile(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = None

    return render(request, "home/profile.html", {"profile": profile})
@login_required
def profile_add_edit(request):
        if request.method== "POST":
           
            user = request.user
            image = request.FILES.get('user_img')
            school =  request.POST.get('school')
            college = request.POST.get('college')
            marital_status = request.POST.get('Marital_status')
            gender = request.POST.get('btnradio')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            print(image)
            if image:
                profile = UserProfile(user=user, user_img=image,school=school, college=college ,phone=phone,gender=gender,marital_status=marital_status,address=address)
                profile.save()
                messages.success(request,"Details Added Successfully")
                return redirect('profile')
            else:
               profile = UserProfile(user=user, school=school, college=college ,phone=phone,gender=gender,marital_status=marital_status,address=address)
               profile.save()
               messages.success(request,"Deatils  Added")
               return redirect('profile')
        
        return render(request, 'home/profile.html', {
       
    })
def author_detail(request, author_id):
   
    author = get_object_or_404(User,id=author_id)
    posts = Post.objects.filter(author=author)
    print(posts)
    # print(profile)
    # profile_details = get_object_or_404(UserProfile,user=)
    #print(profile_details)
     # Get all posts by this author
    # print(posts)
    return render(request, 'home/author_details.html', {'author': author,'posts':posts} )
def update_profile(request, profile_id):
    profile = get_object_or_404(UserProfile, id=profile_id)
    
    if request.method == "POST":
        # Extract data from request.POST and update each field
        profile.school = request.POST.get('school', profile.school)
        profile.college = request.POST.get('college', profile.college)
        profile.user_img = request.FILES.get('user_img',profile.user_img)
        profile.marital_status = request.POST.get('Marital_status', profile.gender)
        profile.gender = request.POST.get('btnradio', profile.gender)
        
        profile.save()      

        
        # Save the updated profile
        
        messages.success(request,"updated successfully")
        # Redirect or send a JSON response
        return redirect('profile')
    
    # return JsonResponse({'message': 'Invalid request method'}, status=400)
    
    