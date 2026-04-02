from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader

from core.models import Product


# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {
        "curso" : "Programação web com django !",
        "outro": "Django é massa para um caralho !",
        "products": products
    }
    return render(request, 'core/index.html', context)

def contact(request):
    return render(request, 'core/contact.html')

def product(request, product_id):
    get_product = get_object_or_404(Product, id=product_id)
    return render(request, "core/product.html", {"product": get_product})

def error404(request, exception):
    template = loader.get_template('core/404.html')
    return HttpResponse(content=template.render(), content_type="text/html", status=404)

def error500(request):
    template = loader.get_template('core/500.html')
    return HttpResponse(content=template.render(), content_type="text/html", status=500)