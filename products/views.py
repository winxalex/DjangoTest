from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import slugify
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm
from taggit.models import Tag
from django.db.models import Q


# Create your views here.
# def hello(request):
#     print(request)
#     #return HttpResponse("Hello World Mile Kitic")
   
#     #return HttpResponse(tags)
#     return render(request,"base.html",{})


 # Create your views here.
def search_by_tags(request):
    print(request)
    #return HttpResponse("Hello World Mile Kitic")
    qparams=request.GET.get('search','')

    if not qparams:
        products=Product.objects.all()
    else:    
        tags=qparams.split()
        #print(tags)
        # my_filter_qs = Q()
        # for tag in tags:
        #     my_filter_qs = my_filter_qs | Q(tags__contains=tag)
        # products=Product.objects.filter(my_filter_qs)
        products=Product.objects.filter(tags__name__in=tags).distinct()
   

    context = {
        'products':products,
       
    }   

    return render(request,"search_view.html",context)  


