# Generated by Django 4.2.8 on 2024-04-08 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modelapp', '0002_notes_content_notes_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='Email',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='user', to='modelapp.users'),
        ),
    ]
