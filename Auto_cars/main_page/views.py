from django.http import FileResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils.http import urlencode

from .models import *
def main_view(request):
    message = request.GET.get('message')
    context = {'message': message}
    return render(request, 'main.html', context)

from django.shortcuts import render
from .models import Car, Characteristics

def show_cars(request):
    cars = Car.objects.select_related('Characteristic').all()
    cars_data = []
    filtered_cars_data = []
    message = ''
    if request.method == 'POST':
        search_text = request.POST.get('search_text')
        mark = request.POST.get('mark')
        status = request.POST.get('status')
        car_type = request.POST.get('type')
        try:
            mileage_ot = int(request.POST.get('mileage_ot'))
        except:
            mileage_ot = 0

        try:
            mileage_do = int(request.POST.get('mileage_do'))
        except:
            mileage_do = 0

        filters = {}
        print(f"{search_text}  {mark}  {status}  {car_type} {mileage_ot} {mileage_do}")
        if search_text:
            filters['model__icontains'] = search_text

        if mark and mark != 'Марка':
            filters['brand__icontains'] = mark
        if status and status != 'Состояние машины':
            filters['Characteristic__car_condition'] = status

        if car_type and car_type != 'Тип кузова':
            filters['Characteristic__car_type'] = car_type
        if mileage_ot and mileage_ot > 1:
            filters['Characteristic__mileage__gte'] = mileage_ot
        if mileage_do and mileage_do > 1:
            filters['Characteristic__mileage__lte'] = mileage_do



        try:
            # Выполнение фильтрации по объединенным условиям
            filtered_cars = Car.objects.filter(**filters)
        except Car.DoesNotExist:
            filtered_cars = Car.objects.none()

        if not filtered_cars.exists():
            message = 'Ничего не найдено'
        else:
            for car in filtered_cars:
                salon = Salon.objects.get(cars=car)
                characteristic = car.Characteristic
                filtered_cars_data.append({'car': car, 'characteristic': characteristic, 'salon': salon})


    for car in cars:
        salon = Salon.objects.get(cars=car)
        characteristic = car.Characteristic
        cars_data.append({'car': car, 'characteristic': characteristic, 'salon': salon})

    state = [
        'Хорошее','После ремонта','Требуется ремонт'
    ]
    car_type = [
        'Купе', 'Пикап', 'Седан','Хэтчбек', 'Лифтбек', 'Фастбек', 'Универсал', 'Кроссовер', 'Внедорожник'
    ]
    car_brand = [
        'Lada', 'Nissan', 'Kia', 'BYD', 'Skoda', 'Tesla', 'Mercedes-Benz', 'Chevrolet', 'Lexus', 'Toyota'
    ]
    return render(request, 'models.html', {'cars_data': cars_data, 'state': state, 'car_type': car_type, 'car_brand': car_brand, 'filtered_cars': filtered_cars_data, 'message': message})


def create_application(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        application = Applications.objects.create(
            name=name,
            email=email,
            number_phone=phone
        )
        application.save()
    params = urlencode({'message': 'Отправлено !'})
    return redirect(f'/?{params}')
def get_car_image(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    image_path = car.image.path
    return FileResponse(open(image_path, 'rb'), content_type='image/jpeg')
