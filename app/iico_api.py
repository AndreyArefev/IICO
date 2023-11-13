from pyiikocloudapi import IikoTransport
import json
from app.models import Product, Category, Modifier
from django.core.exceptions import ObjectDoesNotExist
from ..settings import api_login


load_dotenv()

class Iico_API:
    '''Класс для работы с API IICO'''
    api_login = 'f552c7d2-22e'
    api = IikoTransport(api_login)

    def __init__(self):
        self.menu = Iico_API.api.nomenclature('16a798f1-410a-4a66-a9cd-d9c6cea4457c')

        self.list_categories = [category for category in self.menu['productCategories']]
        self.dict_category_id = {category['id']: category['name'] for category in self.list_categories}
        self.list_products = [product for product in self.menu['products']]
        self.dict_product_id = {a['id']: {'id': a['id'], 'name': a['name']} for a in self.list_products}

    @property
    def all_products(self):
        '''Получение меню в виде JSON'''
        all_products = {product['id']: {'category': self.dict_category_id.get(product['productCategoryId']),
                                        'name': product['name'],
                                        'weight': product['weight'],
                                        'energyAmount': product['energyAmount'],
                                        'energyFullAmount': product['energyFullAmount'],
                                        'currentPrice': product['sizePrices'][0]["price"]["currentPrice"],
                                        'description': product['description'],
                                        'proteinsAmount': product['proteinsAmount'],
                                        'fatAmount': product['fatAmount'],
                                        'carbohydratesAmount': product['carbohydratesAmount'],
                                        'proteinsFullAmount': product['proteinsFullAmount'],
                                        'fatFullAmount': product['fatFullAmount'],
                                        'carbohydratesFullAmount': product['carbohydratesFullAmount'],
                                        'imageLinks': product['imageLinks'],
                                        'modifiers': [self.dict_product_id.get(mod['id']) for mod in product['modifiers']]
                                        } for product in self.menu['products']}
        return all_products

    @property
    def all_products_for_frontend(self):
        '''Получение меню в виде JSON для фронтенда'''
        keys = self.dict_category_id.values()
        response_json = None
        my_dict = dict.fromkeys(keys, None)
        for product in self.menu['products']:
            category = self.dict_category_id.get(product['productCategoryId'])
            if category:
                my_product = {'id': product['id'],
                              'name': product['name'],
                              'weight': product['weight'],
                              'energyAmount': product['energyAmount'],
                              'energyFullAmount': product['energyFullAmount'],
                              'currentPrice': product['sizePrices'][0]["price"]["currentPrice"],
                              'description': product['description'],
                              'proteinsAmount': product['proteinsAmount'],
                              'fatAmount': product['fatAmount'],
                              'carbohydratesAmount': product['carbohydratesAmount'],
                              'proteinsFullAmount': product['proteinsFullAmount'],
                              'fatFullAmount': product['fatFullAmount'],
                              'carbohydratesFullAmount': product['carbohydratesFullAmount'],
                              'additionalInfo': product['additionalInfo'],
                              'imageLinks': product['imageLinks'],
                              'modifiers': [self.dict_product_id.get(mod['id']) for mod in product['modifiers']]
                              }
                if not my_dict[category]:
                    my_dict[category] = [my_product]
                else:
                    my_dict[category].append(my_product)
                list_dict = [{"category_name": key, "items": value} for key, value in my_dict.items()]
                response_json = {"menu": list_dict}
        return response_json

    def load_menu_in_file(self):
        '''Выгрузка меню в файл'''
        with open('all_menu.json', 'w', encoding='UTF-8') as f:
            json.dump(self.all_products_for_frontend, f, ensure_ascii=False)

    def create_models_products_with_iico(self):
        '''Создание моделей продуктов в БД на основе выгрузки из IICO'''
        for p in self.menu['products']:
            queryset_product = Product.objects.filter(iico_id=p['id'])
            product = queryset_product.first()
            if p['imageLinks']:
                imageLinks = p['imageLinks'][0]
            else:
                imageLinks = None
            print(p)
            print(product)
            if not product:
                queryset_category = Category.objects.filter(iico_id=p['productCategoryId'])
                category = queryset_category.first()
                if not category:
                    category = Category.objects.get(name='Без категории')
                else:
                    print(category.name)
                product = Product(iico_id=p['id'],
                                    category=category,
                                    name=p['name'],
                                    weight=p['weight'],
                                    energyAmount=p['energyAmount'],
                                    energyFullAmount=p['energyFullAmount'],
                                    currentPrice=p['sizePrices'][0]["price"]["currentPrice"],
                                    description=p['description'],
                                    proteinsAmount=p['proteinsAmount'],
                                    fatAmount=p['fatAmount'],
                                    carbohydratesAmount=p['carbohydratesAmount'],
                                    proteinsFullAmount=p['proteinsFullAmount'],
                                    fatFullAmount=p['fatFullAmount'],
                                    carbohydratesFullAmount=p['carbohydratesFullAmount'],
                                    additionalInfo=p['additionalInfo'],
                                    imageLinks=imageLinks,
                                  )
                #product.save()
            else:
                queryset_product.update(name=p['name'],
                                       currentPrice=p['sizePrices'][0]["price"]["currentPrice"],
                                       description=p['description'],
                                       additionalInfo=p['additionalInfo'])
            product.save()
            list_modifiers = []
            for m in p['modifiers']:
                queryset_modifier = Modifier.objects.filter(iico_id=m['id'])
                modifiers = queryset_modifier.first()
                if not modifiers:
                    modifiers = Modifier(iico_id=self.dict_product_id.get(m['id'])['id'],
                                             name=self.dict_product_id.get(m['id'])['name'])
                    modifiers.save()
                list_modifiers.append(modifiers)
            product.modifiers.set(list_modifiers)



    def create_models_categories_from_iico(self):
        '''Создание моделей категорий в БД на основе выгрузки из IICO'''
        for c in self.list_categories:
            new_category = Category(iico_id=c['id'], name=c['name'])
            new_category.save()

    def update_models_categories_from_iico(self):
        '''Обновление моделей категорий в БД на основе выгрузки из IICO'''
        for c in self.list_categories:
            try:
                Category.objects.get(name=c['name'])
            except ObjectDoesNotExist:
                new_category = Category(iico_id=c['id'], name=c['name'])
                new_category.save()

