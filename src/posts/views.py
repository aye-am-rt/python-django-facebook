from urllib.parse import quote, quote_plus
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm




# Create your views here.

# posts = [
#     {
#         'author': 'CoreyMS',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'August 27, 2119'
#     },
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'August 28, 2119'
#     }
# ]

# def home(request):
#     context = {
#         'posts': posts
#     }
#     return render(request, 'blog/home.html', context)


def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    if not request.user.is_authenticated():
        raise Http404
    form=PostForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user=request.user
            print(form.cleaned_data)
            instance.save()
            messages.success(request,"Successfully Created !!")
            return HttpResponseRedirect(instance.get_absolute_url())
        else:
            messages.error(request,"Invalid form submission.Try Again.")
        
        print(request.POST)
        print(request.POST.get('title'))
        print(request.POST.get('content'))
    context={'title':'Post Create Page', 'form':form}
    return render(request, 'post_form.html', context)



def post_detail(request, slug=None):
   # instance=Post.objects.get(id=3) this is tight method what if id =3 does not exist you will get error.
   # thats why you have to use get objrect or 404 method.

   instance=get_object_or_404(Post,slug=slug)
   share_string=quote_plus(instance.content)
   context = {'title': ' detail page', 'instance' : instance, 'share_string':share_string}
   return render(request, 'post_detail.html', context)

def post_list(request):
    #instance=get_object_or_404(Post,slug=1)
    queryset_list=Post.objects.all()        # .order_by('-timestamp')  # you can also update this oder in post model class by making class Meta
    print(queryset_list)
    paginator = Paginator(queryset_list, 3) # Show 3 contacts per page.
    page_req_var = 'abc'
    page_number = request.GET.get(page_req_var)
    page_obj = paginator.get_page(page_number)
    context = {
        'object_list': page_obj,
        'title': 'index page',
        'page_req_var': page_req_var,
     }
    return render(request, 'post_list.html', context)
    # return HttpResponse('<h1> post list page </h1>')




def post_update(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance=get_object_or_404(Post,slug=slug)
    form=PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get('title'))
        instance.save()
        messages.success(request,"<a href='#'>Successfully</a> Updated and Saved !!",extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {'title' : instance.title, 'instance' : instance, 'form' : form}
    return render(request, 'post_form.html', context)

def post_delete(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance=get_object_or_404(Post,slug=slug)
    instance.delete()
    messages.success(request,"<a href='#'>Successfully</a> Deleted !!",extra_tags='html_safe')
    return redirect('posts:list')
