from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
from .models import KirrURL
from .forms import SubmitUrlForm
# Create your views here.

class HomeView(View):
    def get(self,request,*args,**kwargs):
        the_form = SubmitUrlForm()
        context = {
            'title' : 'The Url',
            'form' : the_form
        }
        return render(request,'shortener/home.html',context)
    def post(self,request,*agrs,**kwargs):
        form = SubmitUrlForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        context = {
            'title' : 'The Url',
            'form' : form
        }
        return render(request,'shortener/home.html',context)


def index(request,shortcode = None):
    #try:
    #    obj = KirrURL.objects.get(shortcode = shortcode)
    #except :
     #   obj = KirrURL.objects.all().first()
    obj = get_object_or_404(KirrURL, shortcode = shortcode)
    #return HttpResponse("hello {}".format(obj.url))
    return HttpResponseRedirect(obj.url)

class VBCIndex(View):
    def get(self,request,shortcode = None,*args,**kwargs):
        obj = get_object_or_404(KirrURL, shortcode = shortcode)
        #return HttpResponse("hello world {}".format(obj.url))
        return HttpResponseRedirect(obj.url)
    def post(self,request,*args,**kwargs):
        return HttpResponse()

        