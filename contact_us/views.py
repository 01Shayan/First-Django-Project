from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse

def about(req):
    template="about.html"
    return render(req, template)

def subscriber(req):
    if req.method == 'POST':
        email = req.POST.get("email", False)
        if email:
            from .models import Subscriber
            se = Subscriber()
            se.email = email
            se.save()
    return redirect("/")

# def cta(req):
#     template="cta.html"
#     return render(req, template)