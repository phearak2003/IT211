# Generated by Django 4.2.2 on 2023-08-13 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_remove_contact_link_remove_contact_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='link',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='contact',
            name='text',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
