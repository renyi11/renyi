# Generated by Django 2.1.4 on 2019-01-04 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190103_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='upload/', verbose_name='图片'),
        ),
    ]
