# Generated by Django 4.1.3 on 2022-11-07 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_bookings_amount_alter_bookingss_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='abc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.TextField()),
                ('email', models.TextField()),
            ],
        ),
    ]
