# Generated by Django 4.2.2 on 2023-08-13 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_alter_department_icon_alter_department_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='link',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='text',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
