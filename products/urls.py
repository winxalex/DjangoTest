from django.urls import path
from . import views

urlpatterns = [
      #path('<str:search>', views.hello,name='hello'),
      #path('',views.hello,name='hello'),
       path('',views.search_by_tags,name='search_by_tags'),
     
      
]