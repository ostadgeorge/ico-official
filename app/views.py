from django.shortcuts import render, redirect
from django.http import JsonResponse
from . import models
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.

def index(req):
    return render(req, 'index.html', context={})


@csrf_exempt
def contact_us(req):
    if req.method != 'POST':
        return redirect('index')

    name = req.POST['name'] if 'name' in req.POST else "null"
    email = req.POST['email'] if 'email' in req.POST else "null@null.com"
    subject = req.POST['subject'] if 'subject' in req.POST else "null"
    text = req.POST['message'] if 'message' in req.POST else "null"
    models.Message(name=name, email=email, subject=subject, content=text).save()

    return redirect('index')


@csrf_exempt
def blog(req):
    return redirect('blog-list', models.BlogCategorie.objects.all()[0].id)


@csrf_exempt
def blog_list(req, cat_id):
    posts = models.BlogPost.objects.filter(blog_categorie_id=cat_id).all()
    categories = models.BlogCategorie.objects.all()
    return render(req, 'blog.html', context={'categories': categories, 'posts': posts})


@csrf_exempt
def post(req, post_id):
    categories = models.BlogCategorie.objects.all()
    post_detail = models.BlogPost.objects.filter(id=post_id).get()
    return render(req, 'post.html', context={'categories': categories, 'post': post_detail})
