from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views import View
from .models import KirrURL
# Create your views here.


def index(request,shortcode = None):
    #try:
    #    obj = KirrURL.objects.get(shortcode = shortcode)
    #except :
     #   obj = KirrURL.objects.all().first()
    obj = get_object_or_404(KirrURL, shortcode = shortcode)
    return HttpResponse("hello {}".format(obj.url))

class VBCIndex(View):
    def get(self,request,shortcode = None,*args,**kwargs):
        obj = get_object_or_404(KirrURL, shortcode = shortcode)
        return HttpResponse("hello world {}".format(obj.url))
