# Generated by Django 4.1 on 2022-10-20 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_bookingss'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='amount',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='bookingss',
            name='amount',
            field=models.TextField(),
        ),
    ]