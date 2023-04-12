from django.shortcuts import render
from django.http import HttpResponse
from . import  models

def helloview(request):
    return HttpResponse('Hello world')


def blogview(request):
    post = models.Post.objects.all()
    context = {
        'post_object': post
    }
    return render(request, 'post.html', context)