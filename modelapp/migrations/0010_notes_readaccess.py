# Generated by Django 2.2.28 on 2024-04-09 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelapp', '0009_remove_notes_readaccess'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='Readaccess',
            field=models.TextField(default=''),
        ),
    ]