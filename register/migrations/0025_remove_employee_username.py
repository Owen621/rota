# Generated by Django 4.0.3 on 2022-10-17 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0024_remove_employee_comp_pass'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='username',
        ),
    ]
