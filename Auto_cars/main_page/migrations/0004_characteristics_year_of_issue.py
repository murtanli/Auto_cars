# Generated by Django 5.0.4 on 2024-05-07 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0003_car_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='characteristics',
            name='year_of_issue',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]