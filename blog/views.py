from django.shortcuts import render
from django import HttpResponse

# Create your views here.
def index(requests):
    return HttpResponse("Hello World")

def post_list(requests):
    return HttpResponse("This is the list of posts")

def post_detail(request, post_id):
    return HttpResponse(f"Displaying post with ID: {post_id}")  