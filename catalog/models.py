from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    """Модель для таблицы Категорий"""
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    """Модель для таблицы Продуктов"""
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    image = models.ImageField('images/', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    date_create = models.DateField(**NULLABLE, verbose_name='Дата создания')
    last_modified_data = models.DateField(**NULLABLE, verbose_name='Дата последнего изменения')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name}: {self.price}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    version_number = models.CharField(**NULLABLE, max_length=50, verbose_name='Номер версии')
    version_name = models.CharField(**NULLABLE, max_length=50, verbose_name='Название версии')
    is_active = models.BooleanField(verbose_name='Признак текущей версии', default=False)

    def __str__(self):
        return f'{self.version_name}/{self.version_number}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
