# Generated by Django 5.1.2 on 2024-10-24 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_userprofile_user_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_img',
            field=models.ImageField(blank=True, default='user/user.png', upload_to='user/'),
        ),
    ]
