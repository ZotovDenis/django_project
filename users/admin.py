from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'phone', 'country', 'is_verificated')
    list_filter = ('country', 'is_verificated')
    search_fields = ('email', 'phone', 'country')
