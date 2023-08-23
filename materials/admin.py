from django.contrib import admin

from materials.models import Material


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'content', 'preview', 'created_date', 'is_published', 'views_count')
    list_filter = ('created_date', 'is_published')
    search_fields = ('title', 'content',)
