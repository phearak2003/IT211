# Generated by Django 4.2.2 on 2023-08-13 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_contact_link2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='link2',
        ),
    ]
