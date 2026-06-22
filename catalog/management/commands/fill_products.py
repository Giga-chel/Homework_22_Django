from django.core.management.base import BaseCommand
from catalog.models import Product, Category

class Command(BaseCommand):
    help = 'Очищает базу и загружает тестовые продукты'

    def handle(self, *args, **options):
        self.stdout.write('Удаление существующих продуктов и категорий...')
        Product.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write('Добавление новых данных...')

        # Создаем категории
        cat1 = Category.objects.create(name='Рассылки', description='Сервисы email-рассылок')
        cat2 = Category.objects.create(name='Телеграм боты', description='Боты для Telegram')
        cat3 = Category.objects.create(name='Полезные утилиты', description='Маленькие помощники')

        # Создаем продукты
        Product.objects.create(name='СуперРассылка', description='Мощный инструмент для массовой рассылки', category=cat1, price=140.00)
        Product.objects.create(name='ТГ Бот-Модератор', description='Автоматическая модерация чатов', category=cat2, price=50.00)
        Product.objects.create(name='ТГ Бот-Рассылчик', description='Рассылка сообщений по каналам', category=cat2, price=75.00)
        Product.objects.create(name='Очиститель текста', description='Удаление лишних символов', category=cat3, price=15.00)

        self.stdout.write(self.style.SUCCESS('Успешно добавлено 3 категории и 4 продукта!'))
