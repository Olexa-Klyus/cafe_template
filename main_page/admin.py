from django.contrib import admin
from .models import Category, Dish


# варіант адмінки на швидкоруч
# admin.site.register(Category)
# admin.site.register(Dish)

# варіант адмінки, щоб таблиця Dish була вкладена в Category(підпорядкована,вбудована)
# створюємо клас
class DishAdmin(admin.TabularInline):
    model = Dish
    # вказуємо поле привязки - спосок, в якому буде назва поля
    raw_id_fields = ['category']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [DishAdmin]
