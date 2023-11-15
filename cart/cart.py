from decimal import Decimal
from django.conf import settings
from app.models import Product

class Cart:
    def __init__(self, request):
        """
 Инициализировать корзину.
 """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
        # сохранить пустую корзину в сеансе
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, override_quantity=False):
        product_pk = str(product.pk)
        if product_pk not in self.cart:
            self.cart[product_pk] = {'quantity': 0, 'price': str(product.currentPrice)}
        if override_quantity:
            self.cart[product_pk]['quantity'] = quantity
        else:
            self.cart[product_pk]['quantity'] += quantity
        self.save()

    def remove(self, product):
        product_pk = str(product.pk)
        if product_pk in self.cart:
            del self.cart[product_pk]
        self.save()

    def __iter__(self):
        """
        Прокрутить товарные позиции корзины в цикле и
        получить товары из базы данных.
        """
        product_ids = self.cart.keys()
        #  получить объекты product и добавить их в корзину
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item


    def save(self):
        # пометить сеанс как "измененный",
        # чтобы обеспечить его сохранение
        self.session.modified = True

    def __len__(self):
        """
        Подсчитать все товарные позиции в корзине.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

     def clear(self):
    #   удалить корзину из сеанса
        del self.session[settings.CART_SESSION_ID]
        self.save()