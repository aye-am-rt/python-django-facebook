from django.db import models
from django.urls import reverse, reverse_lazy

# Create your models here.
# MVC - model view controller

def upload_location(instance, filename):
    return '%s%s'%(instance.id,filename)

class Post(models.Model):
    title=models.CharField(max_length=100)
    height_field=models.IntegerField(default=0)
    width_field=models.IntegerField(default=0)
    # image=models.FileField(null=True, blank=True)  this was old working , below using image after installing pillow.
    image=models.ImageField(null=True, blank=True, upload_to=upload_location,
                            height_field='height_field', width_field='width_field')
    content=models.TextField()
    updated=models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)

    #if this method is not defined manually django will show post object 1 in admin site.
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"id": self.id})
    
    class Meta:
        ordering = ['-timestamp', '-updated']
    
