# Generated by Django 4.2.4 on 2023-08-22 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='slug',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Slug'),
        ),
    ]