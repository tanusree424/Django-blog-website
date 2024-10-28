from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required ,permission_required
from django.http import HttpResponse 
from .models import Post,Comment, CustomUser,PostView
from django.views.generic import DetailView
from django.contrib import messages
from django.contrib.auth.models import User
from home.models import UserProfile
from django.core.paginator import Paginator
from django.db.models import F
def get_client_ip(request):
    """Get client IP address from request."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
# Create your views here.
def blogHome(request):
    posts  = Post.objects.all().order_by("-sno")
    post_list = Post.objects.all().order_by('-sno')  # Order by latest posts
    paginator = Paginator(post_list, 3)  # Show 3 posts per page

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, 'blog/blog.html', {'posts': posts})

def blogPost(request, slug):
    # Get the post based on the slug instead of post_id
    
    # Get the post based on the slug
    post = get_object_or_404(Post, slug=slug)
    
    # Get the client's IP address
    client_ip = get_client_ip(request)
    
    # Check if this IP has already viewed the post
    if not PostView.objects.filter(post=post, ip_address=client_ip).exists():
        # Increment the view count using F expressions
        post.view = F(('view') + 1)
        post.save(update_fields=['view'])

        # Register the IP address
        PostView.objects.create(post=post, ip_address=client_ip)
    
    # Fetch top-level comments (those without a parent)
    comments = Comment.objects.filter(post=post, parent=None).order_by('-timestamps')
    
    # Context data to pass to the template
    context = {
        'posts': post,
        'comments': comments,
    }

    # Render the template with context
    return render(request, "blog/blogPost.html", context)

def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Post.objects.get(sno=postSno)
        parent = request.POST.get("parentsno")
        
        if  parent =="":
            print(post)
            if not comment:
                messages.error(request,"Please write a Comment here!")
            else:

                comments = Comment(comment=comment, user=user, post=post)   
                comments.save()
                messages.success(request,"Your Comment has been posted")  
                
        else:
             parent = Comment.objects.get(sno=parent)
             comments = Comment(comment=comment, user=user, post=post, parent=parent)   
             comments.save()
             messages.success(request,"Your Reply has been posted")     

    return redirect(f"/blog/{post.slug}")
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, sno=comment_id)
    post = comment.post
    # Check if the logged-in user is the owner of the comment
    if comment.user == request.user:
        comment.delete()
        messages.success(request, "Comment deleted successfully.")
    else:
        messages.error(request, "You are not authorized to delete this comment.")

    # Redirect to the post detail page or wherever you want
    return redirect(f"/blog/{post.slug}")
@login_required
def edit_comment(request):

   

    # Check if the logged-in user is the author of the comment or reply
    # if comment.user != request.user:
    #     messages.error(request, "You are not authorized to edit this comment.")
    #     return redirect("blogPost", slug=comment.post.slug)

    if request.method == "POST":
        # Get the updated content for the comment or reply
        new_comment_text = request.POST.get("reply")
        
        rep_id = request.POST.get("parentsno")
        comment = get_object_or_404(Comment, sno=rep_id)
        
        if new_comment_text:
            comment.comment = new_comment_text  # Update the comment/reply
            comment.save()
            messages.success(request, "Comment updated successfully.")
            return redirect("blogPost", slug=comment.post.slug)
      
              
        else:
            messages.error(request, "Comment cannot be empty.")
            return redirect("blogPost", slug=comment.post.slug)  # Redirect back to the edit page

    # Render the edit form for a GET request
    # context = {"comment": comment}
    # return render(request, "blog/edit_comment.html", context)

@login_required
def delete(request, comment_id):
    comment = get_object_or_404(Comment, sno=comment_id)
    post = comment.post
    # Check if the logged-in user is the owner of the comment
    if comment.user == request.user:
        comment.delete()
        messages.success(request, "Comment deleted successfully.")
    else:
        messages.error(request, "You are not authorized to delete this comment.")

    # Redirect to the post detail page or wherever you want
    return redirect(f"/blog/{post.slug}")
@login_required
def edit_comment_2(request):
    if request.method == "POST":
        comment_id = request.POST.get('parentsno')
        new_text_comment = request.POST.get('comment')
        comment = get_object_or_404(Comment,sno=comment_id)
        if new_text_comment:
            comment.comment =new_text_comment
            comment.save()
            messages.success(request, "Comment updated successfully.")
            return redirect("blogPost", slug=comment.post.slug)
        else:
            messages.error(request, "Comment not updated successfully.")
            return redirect("blogPost", slug=comment.post.slug)
@permission_required('blog.can_view_post', raise_exception=True)
def author_view(request):
    # Author's view logic here

    @permission_required('blog.can_edit_own_post', raise_exception=True)
    def edit_own_post(request, post_id):
        post = get_object_or_404(Post, id=post_id, author=request.user)

    


    
