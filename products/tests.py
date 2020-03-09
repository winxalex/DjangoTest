from django.test import TestCase
from .models import Product
from datetime import date
from django.test import Client
from .views import search_by_tags
from taggit.managers import TaggableManager,TaggedItem
# Create your tests here.


class ProductTestCase(TestCase):
    def setUp(self):
        print('setUP')
       
        product=Product(title="Продукт Тест", description="Опис на тест продукт",published=date.today())
        product.save(force_insert=True)
        product.tags.add("црвена","маичка","адидас")
       

    def test_orm(self):
        product = Product.objects.get(title="Продукт Тест")
        self.assertIsNotNone(product,"Product doesn't exist in ORM")
       
    def test_search(self):
        client=Client()
        response = client.get('/products/?search=маичка црвена')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search_view.html')
        self.assertContains(response, 'Продукт Тест')
            
        product=Product.objects.filter(tags__name__in=['маичка', 'црвена']).first()
        self.assertIsNotNone(product,"Product doesn't returned")
      
        
      
     