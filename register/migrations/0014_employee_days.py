# Generated by Django 4.0.3 on 2022-10-11 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0013_alter_employee_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='days',
            field=models.CharField(default=0, max_length=20),
        ),
    ]
