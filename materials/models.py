from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Material(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='previews/', **NULLABLE, verbose_name='Превью')
    created_date = models.DateField(verbose_name='Дата создания', **NULLABLE)
    is_published = models.BooleanField(default=False, verbose_name='Признак публикации')
    views_count = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')
    slug = models.CharField(max_length=150, **NULLABLE, verbose_name='Slug')

    def __str__(self):
        return f'{self.title}: {self.views_count} просмотров.'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'