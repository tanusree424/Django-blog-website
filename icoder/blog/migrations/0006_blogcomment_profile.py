# Generated by Django 5.1.2 on 2024-10-23 15:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blogcomment'),
        ('home', '0006_alter_userprofie_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcomment',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.userprofie'),
        ),
    ]