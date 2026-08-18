from django.urls import path
from . import views

app_name="blog"
urlpatterns = [
    path("", views.index, name="index"),
    path("post/<str:post_id>", views.postDetail, name="postDetail" ),
    path("old_url/", views.old_redirect_url, name="old_url"),
    path("new_page/", views.new_redirect_url, name="new_page_url"),
]