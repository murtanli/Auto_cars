from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
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

        sel_car = request.POST.get('car')

        application = Applications.objects.create(
            name=name,
            email=email,
            number_phone=phone,
            selected_car=sel_car
        )
        application.save()
    params = urlencode({'message': 'Отправлено !'})
    return redirect(f'/?{params}')
def get_car_image(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    image_path = car.image.path
    return FileResponse(open(image_path, 'rb'), content_type='image/jpeg')


def photo_and_video(request):
    return render(request, 'photo_video.html')

def buyers(request):
    return render(request, "request.html")

def about(request):
    return render(request, "about.html")

def contacts(request):
    return render(request, "contacts.html")


def auth(request):
    if request.method == 'POST':
        login_username = request.POST.get('login')  # Переименуйте переменную login
        password = request.POST.get('password')
        user = authenticate(username=login_username, password=password)  # Используйте новое имя переменной
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            messages.error(request,'Неверный логин или пароль')

    return render(request, "auth.html", )


def sign_in(request):
    if request.method == 'POST':
        login_text = request.POST.get('login')
        password_text = request.POST.get('password')

        try:
            # Создаем пользователя
            user = User.objects.create_user(username=login_text, password=password_text)

            messages.success(request, 'Регистрация прошла успешно!')
            return redirect('auth')

        except:
            messages.error(request, 'Ошибка регистрации. Пользователь с таким логином уже существует.')

        return redirect('sign_in')

    else:
        return render(request, 'sign_in.html')

def logout_view(request):
    logout(request)
    return redirect('main')