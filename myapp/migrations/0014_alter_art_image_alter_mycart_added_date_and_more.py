# Generated by Django 4.0.3 on 2022-06-12 05:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_auto_20200524_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='image',
            field=models.ImageField(upload_to='D:\\python\\codes\\Codes\\Django Project\\testing\\3\\projectenv\\src\\media'),
        ),
        migrations.AlterField(
            model_name='mycart',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 12, 11, 26, 0, 323564)),
        ),
        migrations.AlterField(
            model_name='myorder',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 12, 11, 26, 0, 323564)),
        ),
    ]