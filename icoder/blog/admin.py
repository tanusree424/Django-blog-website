from django.contrib import admin
from django.db import models
from tinymce.widgets import TinyMCE
from .models import Post,Comment

class PostAdmin(admin.ModelAdmin):
    # Override the widget for the 'content' field to use TinyMCE
   formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
   }
   
   list_display = ('title', 'author', 'timestamps', 'view')
   search_fields = ('title', 'author__username')  # Allows searching by author's username
   list_filter = ('author', 'timestamps') 
   def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if not request.user.is_superuser:
            # Remove fields from form for authors
            form.base_fields.pop('some_field_to_hide', None)
        return form

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)