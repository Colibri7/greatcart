from django.contrib import admin

from category.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ['category_name', 'slug']
    search_fields = ['category_name', 'slug']
    list_filter = ['created_at']



