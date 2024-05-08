from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import *
@admin.register(Characteristics)
class CharacteristicsAdmin(admin.ModelAdmin):
    list_display = ('pk','year_of_issue', 'mileage', 'car_condition', 'car_owners', 'Description', 'car_type')

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('pk', 'car_image', 'brand', 'model', 'price', 'Characteristic')

    def car_image(self, obj):
        # Отображение изображения в админке
        if obj.image:
            car_id = obj.pk
            url = reverse('get_car_image', args=[car_id])
            return format_html('<img src="{}" alt="Image" style="max-width: 100px; max-height: 100px;" />', url)
        return None

    car_image.short_description = 'Image Preview'

@admin.register(Managers)
class ManagersAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'lastname', 'salary')

@admin.register(Salon)
class SalonAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'address', 'cars_list', 'managers_list')


    def cars_list(self, obj):
        return ", ".join([f"{car.brand} {car.model}" for car in obj.cars.all()])

    def managers_list(self, obj):
        return ", ".join([f"{manager.name} {manager.lastname}" for manager in obj.managers.all()])

    cars_list.short_description = 'Cars'
    managers_list.short_description = 'Managers'

@admin.register(Applications)
class ApplicationsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'selected_car', 'status', 'name', 'email', 'number_phone')