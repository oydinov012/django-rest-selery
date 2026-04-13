from django.shortcuts import render
from django.http import HttpResponse
from .tasks import my_tast

def tets_view(req):
    my_tast.delay('salom')

    
    return HttpResponse("<h1> HelloWord <h1>")


