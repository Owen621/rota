# Generated by Django 4.0.3 on 2022-10-07 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0010_alter_company_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_pass',
            field=models.CharField(max_length=20),
        ),
    ]