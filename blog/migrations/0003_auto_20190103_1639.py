# Generated by Django 2.1.4 on 2019-01-03 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190103_1608'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content_type',
            new_name='blog_type',
        ),
    ]
