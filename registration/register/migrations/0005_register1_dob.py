# Generated by Django 4.0.3 on 2022-03-09 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_alter_register1_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='register1',
            name='DOB',
            field=models.DateField(blank=True, null=True),
        ),
    ]