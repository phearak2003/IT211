# Generated by Django 4.2.2 on 2023-08-31 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.TextField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10),
        ),
    ]
