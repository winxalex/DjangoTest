from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from taggit.models import Tag
from django.db.models import Q


# Create your views here.
# def hello(request):
#     print(request)
#     #return HttpResponse("Hello World Mile Kitic")
   
#     #return HttpResponse(tags)
#     return render(request,"base.html",{})


# return products containing tags or all products if not search query params are supplied
def search_by_tags(request):

    qparams=request.GET.get('search','')

    if not qparams:
        products=Product.objects.all()
    else:    
        tags=qparams.split()
        products=Product.objects.filter(tags__name__in=tags).distinct()
   

    context = {
        'products':products,
    }   

    return render(request,"search_view.html",context)  


