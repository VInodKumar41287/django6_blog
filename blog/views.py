import logging
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse
import logging
from .models import Post, AboutUs
from django.core.paginator import Paginator
from .forms import ContactForm

# posts = [
#     {'id': 1, 'title': "Post 1", 'content': "Content for Post 1"},
#     {'id': 2, 'title': "Post 2", 'content': "Content for Post 2"},
#     {'id': 3, 'title': "Post 3", 'content': "Content for Post 3"}, 
#     {'id': 4, 'title': "Post 4", 'content': "Content for Post 4"}, 
#     {'id': 5, 'title': "Post 5", 'content': "Content for Post 5"}        
# ]
# Create your views here.
def index(request):
    blog_title = "Latest Posts"
    head_title = "Blog Posts"
    all_posts = Post.objects.all()

    # Pagination
    paginator = Paginator(all_posts, 5)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    return render(request, "blog/index.html", 
                  {
                    'blog_title': blog_title,
                    'head_title': head_title,
                    'page_object': page_object
                  }
                )

def postDetail(request, slug):
    #Stattic Data and Logger
    # post = next((item for item in posts if item['id'] == int(post_id)), None)
    # logger = logging.getLogger("TESTING")
    # logger.debug(f'Post Detail Status: {post}')
    
    # Getting data by POST ID
    try:
        post = Post.objects.get(slug=slug)
        related_posts = Post.objects.filter(category=post.category).exclude(pk=post.id)
    except Post.DoesNotExist:
        raise Http404("POST Doesn't Exists, Please Try with some other...")
    return render(request, "blog/detail.html", {'post': post, 'related_posts': related_posts})

def old_redirect_url(request):
    return redirect(reverse("blog:new_page_url"))

def new_redirect_url(request):
    return HttpResponse("Welcome we are in New URL! New")

def contact_view(request):
    logger = logging.getLogger("TESTING")
    if(request.method == 'POST'):
        form = ContactForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        logger.debug(f' Name is: {name}, Email is: {email}, Message is: {message}')
        if form.is_valid():
            logger.debug(f' Form Data is {form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['message']}')
            success_message = 'Your Email has been sent'
            # sent mail and DB storage
            return render(request, "blog/contact.html",  {'form': form, 'success_message': success_message})
        else:
            logger.debug(f'Form is Not Valid')
            return render(request, "blog/contact.html",  {'form': form, 'name': name, 'email': email, 'message': message})

    return render(request, "blog/contact.html")

def about_view(request):
    about_content = AboutUs.objects.first().content
    return render(request, "blog/about.html", {'about_content': about_content})