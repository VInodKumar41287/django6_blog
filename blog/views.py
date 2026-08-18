from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def index(request):
    blog_title = "Latest Posts"
    head_title = "Blog Posts"
    posts = [
        {'id': 1, 'title': "Post 1", 'content': "Content for Post 1"},
        {'id': 2, 'title': "Post 2", 'content': "Content for Post 2"},
        {'id': 3, 'title': "Post 3", 'content': "Content for Post 3"}, 
        {'id': 4, 'title': "Post 4", 'content': "Content for Post 4"}, 
        {'id': 5, 'title': "Post 5", 'content': "Content for Post 5"}        
    ]
    return render(request, "blog/index.html", 
                  {
                    'blog_title': blog_title,
                    'head_title': head_title,
                    'posts': posts
                  }
                )

def postDetail(request, post_id):
    return render(request, "blog/detail.html")

def old_redirect_url(request):
    return redirect(reverse("blog:new_page_url"))

def new_redirect_url(request):
    return HttpResponse("Welcome we are in New URL! New")
