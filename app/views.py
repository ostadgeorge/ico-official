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
