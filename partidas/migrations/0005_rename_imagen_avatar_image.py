# Generated by Django 5.0.4 on 2024-04-29 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partidas', '0004_rename_image_avatar_imagen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avatar',
            old_name='imagen',
            new_name='image',
        ),
    ]