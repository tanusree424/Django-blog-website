# Generated by Django 5.1.2 on 2024-10-24 04:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_blogcomment_parent_remove_blogcomment_post_and_more'),
        ('home', '0006_alter_userprofie_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_img', models.ImageField(upload_to='user/')),
                ('school', models.CharField(max_length=200)),
                ('college', models.CharField(default='', max_length=200)),
                ('phone', models.CharField(default='', max_length=200)),
                ('address', models.TextField(default='')),
                ('marital_status', models.CharField(default='', max_length=200)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='', max_length=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='UserProfie',
        ),
    ]
