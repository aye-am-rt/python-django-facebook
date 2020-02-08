from django.contrib import admin

# Register your models here.
# customization to admin using modelAdmin can be done.
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ['__str__','title','updated','timestamp']
    list_display_links = ['updated']
    list_editable=['title']
    list_filter = ['updated','timestamp']
    search_fields = ['title','content']
    class Meta:
        model=Post

# admin.site.register(Post)   # old one basic one

admin.site.register(Post, PostModelAdmin)

