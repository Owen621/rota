# Generated by Django 4.0.3 on 2022-10-07 14:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('register', '0008_alter_company_user_alter_employee_hours_per_week_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_name',
            field=models.CharField(default=0, max_length=30),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_pass',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='company',
            name='user',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
