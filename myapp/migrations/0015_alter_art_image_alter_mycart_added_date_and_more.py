# Generated by Django 4.0.3 on 2022-06-12 06:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_alter_art_image_alter_mycart_added_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='image',
            field=models.ImageField(upload_to='D:\\python\\codes\\Codes\\Django Project\\#7 Ecommerce\\projectenv\\src\\media'),
        ),
        migrations.AlterField(
            model_name='mycart',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 12, 11, 47, 23, 910614)),
        ),
        migrations.AlterField(
            model_name='myorder',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 12, 11, 47, 23, 910614)),
        ),
    ]
