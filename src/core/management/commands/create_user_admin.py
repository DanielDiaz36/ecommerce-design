# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from core.models import UserCategory
from users.models.user import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    args = ''
    help = "Type 'manage.py setup --help' for usage."

    def handle(self, *args, **options):

        try:
            User.objects.get(username='admin')
            print("\nYa se encuentra registrado el usuario 'admin'")
        except:
            print("\nCreando usuario administrador.")

            User.objects.create_superuser(
                id=1,
                username='admin',
                first_name='System',
                last_name='Administrator',
                email='admin@admin.cu',
                password='m4ndr4k3',
                is_active=True,
                is_staff=True,
                is_superuser=True,
                user_category=UserCategory.objects.get(id=1),
            ).save()

            print("\nUsuario 'admin' creado con éxito......\n")
