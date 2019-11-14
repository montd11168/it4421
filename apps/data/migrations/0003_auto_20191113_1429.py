# Generated by Django 2.2.7 on 2019-11-13 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20191109_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.SmallIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='promotional_price',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='retail_price',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='voting',
            field=models.FloatField(blank=True, default=5),
        ),
        migrations.AlterField(
            model_name='vote',
            name='value',
            field=models.SmallIntegerField(default=5),
        ),
    ]
