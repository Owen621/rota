# Generated by Django 4.0.3 on 2022-10-17 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0021_alter_employee_company_pass'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='company_pass',
            new_name='comp_pass',
        ),
    ]