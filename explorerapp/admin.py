from django.contrib import admin
from .models import City, Category, Place, Address

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category',  'created', 'updated']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['street', 'city', 'location_number']
    search_fields = ['city']

