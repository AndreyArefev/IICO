from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from app.models import Product
from cart.cart import Cart
from cart.forms import CartAddProductForm

@require_POST
def cart_add(request, product_id):
    cart=Cart(request):
    product = Product.object.get_object_or_404(product_id)
    form = CartAddProductForm(requered.Post)
    if form.is_valid:
        cart.add(self, product, quantity=form.cleaned_data['quantity'], 
                                override_quantity=form.cleaned_data[override_quantity])
    return redirect('cart:cart_detail')

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
                                                                'quantity': item['quantity'],
                                                                'override': True})
    return render(request, 'cart/detail.html', {'cart': cart})
