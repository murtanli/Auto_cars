from django.urls import path
from .views import *

urlpatterns = [
    path('', main_view, name='main'),
    path('cars/', show_cars, name='show_cars'),
    path('buyers/', buyers, name='buyers'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('photo_and_video/', photo_and_video, name='photo_and_video'),
    path('create_application/', create_application, name='create_application'),
    path('car_image/<int:car_id>/', get_car_image, name='get_car_image'),
]
