from django.contrib import admin

from .models import Category, Product

''' Если нужно не только удалять но другие действия то добавляем '''


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


'''И далее эту функцию пдключаем нже в классе'''


class ProductAdmin(admin.ModelAdmin):
    '''Список продкуктов, для того чтобы вносить изменения в админке, база данных не изменится'''
    list_display = ['name', 'category', 'quantity']
    ordering = ['category', '-quantity']  # автоматичекска сортировка в админке
    list_filter = ['date_added', 'price']  # добавление фильтра
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (description)'
    actions = [reset_quantity]

    """Отдельный продукт. Настройка отображения """
    # fields = ['name', 'description', 'category', 'date_added', 'rating']
    readonly_fields = ['date_added', 'rating']
    fieldsets = [  # Филд сет конфликтует с филд, поэтому их в 26 строке коментируем
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],  # поле должно быть схлопнуто
                'description': 'Категория товара и его подробное описание',
                'fields': ['category', 'description'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'quantity'],
            }
        ),
        (
            'Рейтинг и прочее',
            {
                'description': 'Рейтинг сформирован автоматически на основе оценок покупателей',
                'fields': ['rating', 'date_added'],
            }
        ),
    ]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
