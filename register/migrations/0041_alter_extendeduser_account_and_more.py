# Generated by Django 4.0.3 on 2022-11-22 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0040_extendeduser_postcode_alter_extendeduser_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendeduser',
            name='account',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='extendeduser',
            name='postcode',
            field=models.CharField(max_length=8),
        ),
    ]