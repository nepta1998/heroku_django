# Generated by Django 3.0.4 on 2020-03-17 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_message', '0008_auto_20200316_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='image',
            field=models.ImageField(default='../media/pictures/default.jpg', max_length=255, upload_to='pictures/%y/%m/%d/'),
        ),
    ]
