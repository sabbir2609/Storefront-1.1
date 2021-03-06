from django.shortcuts import get_list_or_404, render
from django.core.paginator import Paginator
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Product
from .serializer import ProductSerializer


@api_view()
def product_list(request):
    queryset = Product.objects.all()
    serializer = ProductSerializer(queryset, many=True)

    return Response(serializer.data)

@api_view()
def product_detail(request, id):
    product = get_list_or_404(Product, pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)




# Template view section

def product_list_template(request):
    queryset = Product.objects.all()
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'store/products.html', {'page_obj': page_obj})
