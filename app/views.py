from django.shortcuts import render, get_object_or_404
from app.models import Product, Category, Modifier


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category,
                                     slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'app/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})

def product_info(request, pk, slag):
    product = get_object_or_404(Product, pk=pk, slag=slag)
    return render (request,
                  'app/product/detail.html',
                  {'product': product})




