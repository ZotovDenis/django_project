import json

from django.core.management import BaseCommand

from catalog.models import Category, Product
from config.settings import BASE_DIR


class Command(BaseCommand):
    file_categories = f'{BASE_DIR}/category_data.json'
    file_products = f'{BASE_DIR}/product_data.json'

    @staticmethod
    def read_json_categories():
        with open(Command.file_categories, 'r', encoding='windows-1251') as f:
            categories_list = json.load(f)
        return categories_list

    @staticmethod
    def read_json_products():
        with open(Command.file_products, 'r', encoding='windows-1251') as f:
            product_list = json.load(f)
        return product_list

    #
    def handle(self, *args, **options):
        Product.objects.all().delete()
        products_for_create = []

        Category.objects.all().delete()
        categories_for_create = []

        for category_item in Command.read_json_categories():
            categories_for_create.append(
                Category(name=category_item['fields']['name'],
                         description=category_item['fields']['description'])
            )

        Category.objects.bulk_create(categories_for_create)
        pk_step = len(Command.read_json_categories())

        for product_item in Command.read_json_products():
            products_for_create.append(
                Product(name=product_item['fields']['name'],
                        description=product_item['fields']['description'],
                        category=Category.objects.get(pk=product_item['fields']['category'] + pk_step),
                        price=product_item['fields']['price'])
            )

        Product.objects.bulk_create(products_for_create)
