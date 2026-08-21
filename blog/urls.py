from django.urls import path
from . import views

app_name="blog"
urlpatterns = [
    path("", views.index, name="index"),
    path("post/<str:slug>", views.postDetail, name="postDetail" ),
    path("old_url/", views.old_redirect_url, name="old_url"),
    path("new_page/", views.new_redirect_url, name="new_page_url"),
    path("contact", views.contact_view, name="contact"),
    path("about", views.about_view, name="about")
]