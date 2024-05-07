from django.urls import path
from .views import *

urlpatterns = [
    path('', main_view, name='main'),
    path('cars/', show_cars, name='show_cars'),
    path('create_application/', create_application, name='create_application'),
    path('car_image/<int:car_id>/', get_car_image, name='get_car_image'),
]
