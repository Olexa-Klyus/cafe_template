from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    # щоб в адмінці відображалася назва категорії, потрібно реалізувати метод str
    def __str__(self):
        return f'{self.title}'

    # щоб в адмінці записи сортувалися, потрібно прописати списком або кортежем атрибути за якими сортуємо
    class Meta:
        ordering = ('position',)



class Dish(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField()
    is_visible = models.BooleanField(default=True)
    ingredients = models.CharField(max_length=255)
    desc = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    photo = models.ImageField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_special = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('category', 'position')
