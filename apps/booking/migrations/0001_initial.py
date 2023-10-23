# Generated by Django 4.2.6 on 2023-10-23 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('room', '0001_initial'),
        ('guest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in_date', models.DateField(auto_now=True)),
                ('check_out_date', models.DateField(blank=True, null=True)),
                ('is_paid', models.BooleanField(default=False)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guest.guest')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.room')),
            ],
            options={
                'verbose_name': 'Брон',
                'verbose_name_plural': 'Брон',
            },
        ),
    ]
