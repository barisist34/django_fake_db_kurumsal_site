from django.shortcuts import render
from django.http import HttpResponse
from random import randint

def home(request):
    # print("request.META:::",request.META)
    #print("request.HEADER:::",request.HEADERS)
    context={"platform":f"Django platformu kullanildi,randint donen veri: {randint(1,100)}"}
    #context={}
    return render(request,"page/home_page.html",context)
    #return HttpResponse("baris")

def oylesine_view(request):
    return HttpResponse("oylesine sayfasi")

def contact_us(request):
    context=dict()
    return render (request,"page/contact_us.html",context)

def about_us(request):
    context=dict()
    return render (request,"page/about_us.html",context)
