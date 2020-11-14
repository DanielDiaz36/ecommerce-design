# Generated by Django 2.2.10 on 2020-11-14 07:16

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=100, verbose_name='nombre')),
                ('last_name', models.CharField(max_length=200, verbose_name='apellidos')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff')),
                ('is_active', models.BooleanField(default=False, verbose_name='activo')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status')),
                ('company', models.CharField(blank=True, max_length=50, null=True, verbose_name='compañía')),
                ('city', models.CharField(blank=True, max_length=50, null=True, verbose_name='ciudad')),
                ('phone_prefix', models.CharField(blank=True, max_length=4, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='teléfono')),
                ('facebook', models.CharField(blank=True, max_length=50, null=True, verbose_name='facebook')),
                ('whatsapp', models.CharField(blank=True, max_length=50, null=True, verbose_name='whatsapp')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='fecha de actualización')),
                ('activated_at', models.DateTimeField(blank=True, null=True, verbose_name='fecha de activación')),
                ('password_changed_at', models.DateTimeField(blank=True, null=True, verbose_name='fecha de cambio de contraseña')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='fecha de eliminación')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='eliminiado')),
                ('locked_at', models.DateTimeField(blank=True, null=True, verbose_name='fecha de deshabilitación')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Country', verbose_name='país')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.UserCategory', verbose_name='categoría de usuario')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'auth_user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
