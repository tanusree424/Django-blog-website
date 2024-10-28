
from django.urls import path,include
from .views import *

urlpatterns = [
    
    path('', blogHome, name="bloghome"),
    path('<str:slug>', blogPost, name="blogPost"),
    path('comment/', postComment, name="comment" ),
    path("reply/edit/",edit_comment, name="edit_comment"),
    path("comment/edit/",edit_comment_2, name="edit_reply"),
    path('delete-comment/<int:comment_id>/', delete_comment, name='delete_comment'),
    path('delete/<int:comment_id>/', delete, name='delete_com'),
  
    # API's to Posting comment
  
]
