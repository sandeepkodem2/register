# Generated by Django 4.0.3 on 2022-03-09 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_register1_email_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='register1',
            name='Flat_No',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='register1',
            name='Gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=100),
        ),
        migrations.AddField(
            model_name='register1',
            name='Phone_Number',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='register1',
            name='Street',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]