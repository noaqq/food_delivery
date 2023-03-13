from django.db import models

CATEGORY_CHOICES = (
    ("Молочная продукция", "Молочная продукция"),
    ("Мясная гастрономия", "Мясная гастрономия"),
    ("Выпечка", "Выпечка"),
    ("Бакалея", "Бакалея"),
    ("Полуфабрикаты", "Полуфабрикаты"),
    ("Напитки", "Напитки"),
    ("Снеки", "Снеки"),
)


class catalog(models.Model):
    name = models.CharField("Название товара", max_length=100)
    category = models.CharField("Категория", choices=CATEGORY_CHOICES, max_length=20)
    price = models.FloatField()
    description = models.CharField("Описание товара", max_length=150)
    expiration_date = models.CharField("Срок годности", max_length=30)
    image = models.ImageField(blank=True, upload_to="static/assets/food")

    def __str__(self):
        return self.name
