# Generated by Django 5.0.4 on 2024-05-08 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0009_applications_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='email',
            field=models.EmailField(blank=True, max_length=40, null=True),
        ),
    ]
