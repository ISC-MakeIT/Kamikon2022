from django.shortcuts import render

# Create your views here.

def log_in(req) :
    return render(req, 'pls/log_in.html', {})