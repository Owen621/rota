# Generated by Django 4.0.3 on 2022-10-17 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0022_rename_company_pass_employee_comp_pass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='comp_pass',
            field=models.ForeignKey(default=0, max_length=20, on_delete=django.db.models.deletion.CASCADE, to='register.company'),
        ),
    ]
