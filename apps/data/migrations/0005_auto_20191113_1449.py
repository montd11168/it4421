# Generated by Django 2.2.7 on 2019-11-13 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20191113_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='voting',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
