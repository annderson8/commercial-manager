from itertools import product
import json
from unicodedata import category

from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import Product


class ProductView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id>0):
            products = list(Product.objects.filter(id=id).values())
            if len(products) > 0:
                product = products[0]
                data = {'message':'Success', 'product': product}
            else:
                data = {'message': 'Product not found'}
            return JsonResponse(data)
        else:
            products = list(Product.objects.values())
            if len(products) > 0:
                data = {'message':'Success', 'products': products}
            else:
                data = {'message': 'Products not found'}
            return JsonResponse(data)

    def post(self, request):
        json_data = json.loads(request.body)
        Product.objects.create(name=json_data['name'], category=json_data['category'], type_product=json_data['type_product'])
        data = {'message': 'Success'}
        return JsonResponse(data)

    def put(self, request, id):
        json_data = json.loads(request.body)
        products = list(Product.objects.filter(id=id).values())
        if len(products) > 0:
            product = Product.objects.get(id=id)
            product.name = json_data['name']
            product.category = json_data['category']
            product.type_product = json_data['type_product']
            product.save()
            data = {'message': 'Success'}
        else:
            data = {'message': 'Product not found'}
        return JsonResponse(data)
    
    def delete(self, request, id):
        products = list(Product.objects.filter(id=id).values())
        if len(products) > 0:
            Product.objects.filter(id=id).delete()
            data = {'message': 'Success'}
        else:
            data = {'message': 'Product not found'}
        return JsonResponse(data)

