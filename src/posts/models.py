from django.db import models
from django.conf import settings
from django.urls import reverse, reverse_lazy
from django.db.models.signals import pre_save
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.
# MVC - model view controller


# post.objects.all()
# post.objects.create(user=user, title='some title')  these are the examples of default postManager class.
# we are overriding it here.
class PostManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(PostManager, self).filter(draft=False).filter(publish__lte=timezone.now())
    # changed function name from all to active because we want to see the published post if we edit it and put it in draft.
    # this function was called in post_list views. to  make queryset_list.

def upload_location(instance, filename):
    return '%s/%s'%(instance.id,filename)

class Post(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE) # blank=True, null=True
    title=models.CharField(max_length=100)
    slug=models.SlugField(unique=True)
    height_field=models.IntegerField(default=0)
    width_field=models.IntegerField(default=0)
    # image=models.FileField(null=True, blank=True)  this was old working , below using image after installing pillow.
    image=models.ImageField(null=True, blank=True, upload_to=upload_location,
                            height_field='height_field', width_field='width_field')
    content=models.TextField()
    draft=models.BooleanField(default=False)                   # these two fields are being added for draft feature.
    publish=models.DateField(auto_now=False, auto_now_add=False)  # before it made facbook comment and like feature git pushed.
    updated=models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)

    objects=PostManager()

    #if this method is not defined manually django will show post object 1 in admin site.
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"slug": self.slug})
    
    class Meta:
        ordering = ['-timestamp', '-updated']

    
def create_slug(instance, new_slug=None):
    slug=slugify(instance.title)       # turn title into slug. eg- Tesla Item 1 --> tesla-item-1
    if new_slug is not None:
        slug=new_slug
    qs=Post.objects.filter(slug=slug).order_by("-id")
    exists=qs.exists()
    if exists:
        new_slug="%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug=create_slug(instance)


pre_save.connect(pre_save_post_receiver, sender=Post)
    
