# Generated by Django 5.1.2 on 2024-10-23 15:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_blogcomment_profile'),
        ('home', '0006_alter_userprofie_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='profile',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.userprofie'),
        ),
    ]
