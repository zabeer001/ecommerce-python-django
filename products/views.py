from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.shortcuts import render, get_object_or_404

def home(request):
    return HttpResponse("Hello World")


def product_list(request):
    # Fetch all products from the database
    products = Product.objects.all()

    # Render the 'product_list.html' template and pass the products to it
    return render(request, 'product_list.html', {'products': products})
    
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})

