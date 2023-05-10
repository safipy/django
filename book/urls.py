from django.urls import path
from book.views import helloview, blogview

urlpatterns = [
    path("hello/", helloview, name="hello"),
    path("post/", blogview, name="post"),
]
