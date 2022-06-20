from django.contrib import admin

from .models import Category, Product, Lesson


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'author', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    raw_id_fields = ('author',)


admin.site.register(Product, ProductAdmin)


class LessonAdmin(admin.ModelAdmin):
    list_display = ['id_product', 'name', 'slug', 'description', 'created', 'updated']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Lesson, LessonAdmin)



