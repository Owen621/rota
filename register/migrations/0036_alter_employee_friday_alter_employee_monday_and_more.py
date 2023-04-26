# Generated by Django 4.0.3 on 2022-11-03 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0035_alter_employee_friday_alter_employee_hourly_pay_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='friday',
            field=models.CharField(choices=[('', ''), ('09:00-22:00', '09:00-22:00'), ('09:00-17:00', '09:00-17:00'), ('10:00-22:00', '10:00-22:00'), ('10:00-17:00', '10:00-17:00'), ('11:00-22:00', '11:00-22:00'), ('11:00-17:00', '11:00-17:00'), ('12:00-22:00', '12:00-22:00'), ('12:00-17:00', '12:00-17:00'), ('13:00-22:00', '13:00-22:00'), ('13:00-17:00', '13:00-17:00'), ('14:00-22:00', '14:00-22:00'), ('15:00-22:00', '15:00-22:00'), ('16:00-22:00', '16:00-22:00'), ('17:00-22:00', '17:00-22:00'), ('18:00-22:00', '18:00-22:00')], default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='employee',
            name='monday',
            field=models.CharField(choices=[('', ''), ('09:00-22:00', '09:00-22:00'), ('09:00-17:00', '09:00-17:00'), ('10:00-22:00', '10:00-22:00'), ('10:00-17:00', '10:00-17:00'), ('11:00-22:00', '11:00-22:00'), ('11:00-17:00', '11:00-17:00'), ('12:00-22:00', '12:00-22:00'), ('12:00-17:00', '12:00-17:00'), ('13:00-22:00', '13:00-22:00'), ('13:00-17:00', '13:00-17:00'), ('14:00-22:00', '14:00-22:00'), ('15:00-22:00', '15:00-22:00'), ('16:00-22:00', '16:00-22:00'), ('17:00-22:00', '17:00-22:00'), ('18:00-22:00', '18:00-22:00')], default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='employee',
            name='saturday',
            field=models.CharField(choices=[('', ''), ('09:00-22:00', '09:00-22:00'), ('09:00-17:00', '09:00-17:00'), ('10:00-22:00', '10:00-22:00'), ('10:00-17:00', '10:00-17:00'), ('11:00-22:00', '11:00-22:00'), ('11:00-17:00', '11:00-17:00'), ('12:00-22:00', '12:00-22:00'), ('12:00-17:00', '12:00-17:00'), ('13:00-22:00', '13:00-22:00'), ('13:00-17:00', '13:00-17:00'), ('14:00-22:00', '14:00-22:00'), ('15:00-22:00', '15:00-22:00'), ('16:00-22:00', '16:00-22:00'), ('17:00-22:00', '17:00-22:00'), ('18:00-22:00', '18:00-22:00')], default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='employee',
            name='sunday',
            field=models.CharField(choices=[('', ''), ('09:00-22:00', '09:00-22:00'), ('09:00-17:00', '09:00-17:00'), ('10:00-22:00', '10:00-22:00'), ('10:00-17:00', '10:00-17:00'), ('11:00-22:00', '11:00-22:00'), ('11:00-17:00', '11:00-17:00'), ('12:00-22:00', '12:00-22:00'), ('12:00-17:00', '12:00-17:00'), ('13:00-22:00', '13:00-22:00'), ('13:00-17:00', '13:00-17:00'), ('14:00-22:00', '14:00-22:00'), ('15:00-22:00', '15:00-22:00'), ('16:00-22:00', '16:00-22:00'), ('17:00-22:00', '17:00-22:00'), ('18:00-22:00', '18:00-22:00')], default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='employee',
            name='thursday',
            field=models.CharField(choices=[('', ''), ('09:00-22:00', '09:00-22:00'), ('09:00-17:00', '09:00-17:00'), ('10:00-22:00', '10:00-22:00'), ('10:00-17:00', '10:00-17:00'), ('11:00-22:00', '11:00-22:00'), ('11:00-17:00', '11:00-17:00'), ('12:00-22:00', '12:00-22:00'), ('12:00-17:00', '12:00-17:00'), ('13:00-22:00', '13:00-22:00'), ('13:00-17:00', '13:00-17:00'), ('14:00-22:00', '14:00-22:00'), ('15:00-22:00', '15:00-22:00'), ('16:00-22:00', '16:00-22:00'), ('17:00-22:00', '17:00-22:00'), ('18:00-22:00', '18:00-22:00')], default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='employee',
            name='tuesday',
            field=models.CharField(choices=[('', ''), ('09:00-22:00', '09:00-22:00'), ('09:00-17:00', '09:00-17:00'), ('10:00-22:00', '10:00-22:00'), ('10:00-17:00', '10:00-17:00'), ('11:00-22:00', '11:00-22:00'), ('11:00-17:00', '11:00-17:00'), ('12:00-22:00', '12:00-22:00'), ('12:00-17:00', '12:00-17:00'), ('13:00-22:00', '13:00-22:00'), ('13:00-17:00', '13:00-17:00'), ('14:00-22:00', '14:00-22:00'), ('15:00-22:00', '15:00-22:00'), ('16:00-22:00', '16:00-22:00'), ('17:00-22:00', '17:00-22:00'), ('18:00-22:00', '18:00-22:00')], default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='employee',
            name='wednesday',
            field=models.CharField(choices=[('', ''), ('09:00-22:00', '09:00-22:00'), ('09:00-17:00', '09:00-17:00'), ('10:00-22:00', '10:00-22:00'), ('10:00-17:00', '10:00-17:00'), ('11:00-22:00', '11:00-22:00'), ('11:00-17:00', '11:00-17:00'), ('12:00-22:00', '12:00-22:00'), ('12:00-17:00', '12:00-17:00'), ('13:00-22:00', '13:00-22:00'), ('13:00-17:00', '13:00-17:00'), ('14:00-22:00', '14:00-22:00'), ('15:00-22:00', '15:00-22:00'), ('16:00-22:00', '16:00-22:00'), ('17:00-22:00', '17:00-22:00'), ('18:00-22:00', '18:00-22:00')], default='', max_length=15),
        ),
    ]