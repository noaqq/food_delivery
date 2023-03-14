from django.db import models

CATEGORY_CHOICES = (
    ("Молоко, яйца, масло", "Молоко, яйца, масло"),
    ("Мясо и птица", "Мясо и птица"),
    ("Выпечка", "Выпечка"),
    ("Бакалея", "Бакалея"),
    ("Полуфабрикаты", "Полуфабрикаты"),
    ("Напитки", "Напитки"),
    ("Чипсы, орехи, сухофрукты", "Чипсы, орехи, сухофрукты"),
)


class catalog(models.Model):
    name = models.CharField("Название товара", max_length=100)
    category = models.CharField("Категория", choices=CATEGORY_CHOICES, max_length=50)
    price = models.IntegerField()
    description = models.CharField("Описание товара", max_length=150)
    expiration_date = models.CharField("Срок годности", max_length=50)
    image = models.ImageField(blank=True, upload_to="delivery/static/assets/food")

    def __str__(self):
        return self.name
