# Generated by Django 4.1 on 2022-10-20 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.TextField()),
                ('email', models.TextField()),
                ('sex', models.TextField()),
                ('dob', models.TextField()),
                ('address', models.TextField()),
                ('cin', models.TextField()),
                ('number', models.TextField()),
                ('cout', models.TextField()),
                ('roomname', models.TextField()),
                ('amount', models.IntegerField()),
                ('mode', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RoomsAvailable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/')),
                ('title', models.TextField(max_length=1000)),
                ('amount', models.IntegerField()),
                ('available', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RoomsList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list', models.TextField()),
                ('fkey', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='app1.roomsavailable', verbose_name='Category')),
            ],
        ),
    ]