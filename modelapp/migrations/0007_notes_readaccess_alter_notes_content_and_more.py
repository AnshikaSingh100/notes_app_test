# Generated by Django 4.2.8 on 2024-04-08 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelapp', '0006_rename_email_notes_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='Readaccess',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='notes',
            name='Content',
            field=models.TextField(default='Sample Content'),
        ),
        migrations.AlterField(
            model_name='notes',
            name='Title',
            field=models.TextField(default='Sample Title'),
        ),
    ]