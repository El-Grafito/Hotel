# Generated by Django 4.2.6 on 2023-10-23 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('last_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('email', models.CharField(blank=True, max_length=255, null=True, verbose_name='Эл. Почта')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='Телефонный номер')),
            ],
            options={
                'verbose_name': 'Гость',
                'verbose_name_plural': 'Гости',
            },
        ),
    ]
