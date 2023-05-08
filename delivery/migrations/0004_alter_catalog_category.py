# Generated by Django 4.1.7 on 2023-05-07 21:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('delivery', '0003_alter_basket_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='category',
            field=models.CharField(
                choices=[
                    ('milk', 'Молоко, яйца, масло'),
                    ('meat', 'Мясо и птица'),
                    ('bake', 'Выпечка'),
                    ('grocery', 'Бакалея'),
                    ('freeze', 'Полуфабрикаты'),
                    ('drinks', 'Напитки'),
                    ('snacks', 'Чипсы, орехи, сухофрукты'),
                ],
                max_length=50,
                verbose_name='Категория',
            ),
        ),
    ]