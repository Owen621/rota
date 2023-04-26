# Generated by Django 4.0.3 on 2022-10-20 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0033_alter_employee_hourly_pay_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='hourly_pay',
            field=models.FloatField(choices=[(5, '£5.00'), (5.5, '£5.50'), (6, '£6.00'), (6.5, '£6.50'), (7, '£7.00'), (7.5, '£7.50'), (8, '£8.00'), (8.5, '£8.50'), (9, '£9.00'), (9.5, '£9.50'), (10, '£10.00'), (10.5, '£10.50'), (11, '£11.00'), (11.5, '£11.50'), (12, '£12.00'), (12.5, '£12.50'), (13, '£13.00'), (13.5, '£13.50'), (14, '£14.00'), (14.5, '£14.50'), (5, '£15.00')]),
        ),
    ]