# Generated by Django 5.0.4 on 2024-05-07 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0004_characteristics_year_of_issue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characteristics',
            name='Description',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
