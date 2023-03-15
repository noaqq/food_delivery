# Generated by Django 4.1.7 on 2023-03-14 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("delivery", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="catalog",
            name="category",
            field=models.CharField(
                choices=[
                    ("Молоко, яйца, масло", "Молоко, яйца, масло"),
                    ("Мясо и птица", "Мясо и птица"),
                    ("Выпечка", "Выпечка"),
                    ("Бакалея", "Бакалея"),
                    ("Полуфабрикаты", "Полуфабрикаты"),
                    ("Напитки", "Напитки"),
                    ("Чипсы, орехи, сухофрукты", "Чипсы, орехи, сухофрукты"),
                ],
                max_length=50,
                verbose_name="Категория",
            ),
        ),
        migrations.AlterField(
            model_name="catalog",
            name="expiration_date",
            field=models.CharField(max_length=50, verbose_name="Срок годности"),
        ),
        migrations.AlterField(
            model_name="catalog",
            name="image",
            field=models.ImageField(
                blank=True, upload_to="delivery/static/assets/food"
            ),
        ),
    ]