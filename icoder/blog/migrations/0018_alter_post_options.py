# Generated by Django 5.1.2 on 2024-10-28 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_alter_post_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'permissions': [('can_view_post', 'Can view post'), ('can_edit_own_post', 'Can edit own post')]},
        ),
    ]