# Generated by Django 4.0.3 on 2022-10-01 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_employee_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='hours_per_week',
            field=models.IntegerField(choices=[(5, 5), (10, 10), (15, 15), (20, 20), (25, 25), (30, 30), (35, 35), (40, 40)], default=10),
        ),
    ]
