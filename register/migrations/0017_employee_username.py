# Generated by Django 4.0.3 on 2022-10-17 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0016_remove_employee_days_employee_friday_employee_monday_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='username',
            field=models.CharField(default=0, max_length=20, verbose_name='Username'),
        ),
    ]