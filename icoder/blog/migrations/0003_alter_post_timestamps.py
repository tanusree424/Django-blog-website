# Generated by Django 5.1.2 on 2024-10-21 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_delete_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timestamps',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
