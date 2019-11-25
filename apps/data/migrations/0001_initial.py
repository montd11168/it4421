# Generated by Django 2.2.7 on 2019-11-24 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.SmallIntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Export',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=0)),
                ('quantity', models.SmallIntegerField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Import',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=0)),
                ('quantity', models.SmallIntegerField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('XÁC NHẬN', 'Xác nhận'), ('ĐANG GIAO', 'Đang giao'), ('ĐÃ GIAO', 'Đã giao'), ('ĐÃ HỦY', 'Đã hủy'), ('TRẢ HÀNG', 'Trả hàng')], default='XÁC NHẬN', max_length=9)),
                ('note', models.TextField(blank=True)),
                ('total', models.BigIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guarantee', models.CharField(blank=True, max_length=255)),
                ('guarantee_des', models.CharField(blank=True, max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('color', models.CharField(blank=True, max_length=255)),
                ('screen', models.CharField(blank=True, max_length=255)),
                ('resolution', models.CharField(blank=True, max_length=255)),
                ('front_camera', models.CharField(blank=True, max_length=255)),
                ('rear_camera', models.CharField(blank=True, max_length=255)),
                ('chip', models.CharField(blank=True, max_length=255)),
                ('ram', models.CharField(blank=True, max_length=255)),
                ('rom', models.CharField(blank=True, max_length=255)),
                ('pin', models.CharField(blank=True, max_length=255)),
                ('operating_system', models.CharField(blank=True, max_length=255)),
                ('charging_port', models.CharField(blank=True, max_length=255)),
                ('retail_price', models.IntegerField(blank=True, default=0)),
                ('listed_price', models.IntegerField(default=0)),
                ('promotional_price', models.IntegerField(blank=True, default=0)),
                ('count', models.SmallIntegerField(default=0)),
                ('voting', models.FloatField(blank=True, default=None, null=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='product')),
                ('description', models.TextField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('logo', models.ImageField(blank=True, upload_to='supplier')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField(default=5)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='data.Product')),
            ],
        ),
    ]
