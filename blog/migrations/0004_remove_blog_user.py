# Generated by Django 4.0.4 on 2022-06-02 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='user',
        ),
    ]