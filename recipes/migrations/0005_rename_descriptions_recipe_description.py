# Generated by Django 5.0.7 on 2024-08-11 01:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_alter_recipe_cover'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='descriptions',
            new_name='description',
        ),
    ]
