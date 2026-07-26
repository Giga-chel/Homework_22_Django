from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product


class Command(BaseCommand):
    help = 'Создает группы Модератор продуктов и Контент-менеджер'

    def handle(self, *args, **options):
        # Группа Модератор продуктов
        mod_group, created = Group.objects.get_or_create(name='Модератор продуктов')

        # Права для модератора продуктов
        unpublish_perm = Permission.objects.get(codename='can_unpublish_product')
        delete_perm = Permission.objects.get(codename='delete_product')

        mod_group.permissions.add(unpublish_perm, delete_perm)

        # Группа Контент-менеджер
        content_group, created = Group.objects.get_or_create(name='Контент-менеджер')
        blog_ct = ContentType.objects.get(app_label='blog', model='blogpost')
        blog_perms = Permission.objects.filter(content_type=blog_ct)
        content_group.permissions.add(*blog_perms)

        self.stdout.write(self.style.SUCCESS('Группы и права успешно созданы!'))
