from django.db import models


class Characteristics(models.Model):
    state = (
        ('Хорошее', 'Хорошее'),
        ('После ремонта', 'После ремонта'),
        ('Требуется ремонт', 'Требуется ремонт')
    )
    car_type = (
        ('Купе', 'Купе'),
        ('Пикап', 'Пикап'),
        ('Седан', 'Седан'),
        ('Хэтчбек', 'Хэтчбек'),
        ('Лифтбек', 'Лифтбек'),
        ('Фастбек', 'Фастбек'),
        ('Универсал', 'Универсал'),
        ('Кроссовер', 'Кроссовер'),
        ('Внедорожник', 'Внедорожник')
    )
    year_of_issue = models.CharField(max_length=4, null=True, blank=True)
    mileage = models.IntegerField()
    car_condition = models.CharField(choices=state, max_length=50)
    car_owners = models.IntegerField()
    Description = models.TextField(max_length=200, null=True, blank=True)
    car_type = models.CharField(choices=car_type, max_length=50)

class Car(models.Model):
    image = models.ImageField(upload_to='car_images/', null=True, blank=True)
    brand = models.CharField(max_length=25)
    model = models.CharField(max_length=50)
    price = models.IntegerField()
    Characteristic = models.ForeignKey(Characteristics, on_delete=models.CASCADE)

class Managers(models.Model):
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    salary = models.CharField(max_length=50)
class Salon(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    cars = models.ManyToManyField(Car, null=True, blank=True)
    managers = models.ManyToManyField(Managers, null=True, blank=True)

class Applications(models.Model):

    status_text = (
        ('Отправлено', 'Отправлено'),
        ('На рассмотрении', 'На рассмотрении'),
        ('Принято', 'Принято')
    )

    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=40, null=True, blank=True)
    number_phone = models.CharField(max_length=20)
    selected_car = models.CharField(max_length=40, null=True, blank=True)
    status = models.CharField(max_length=20, choices=status_text, default='Отправлено')
