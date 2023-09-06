# Generated by Django 4.2.4 on 2023-09-05 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='Номер версии')),
                ('version_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Название версии')),
                ('is_active', models.BooleanField(default=False, verbose_name='Признак текущей версии')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Версия',
                'verbose_name_plural': 'Версии',
            },
        ),
    ]