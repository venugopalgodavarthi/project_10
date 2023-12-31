# Generated by Django 4.2.7 on 2023-11-10 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_cart_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='order_food',
            fields=[
                ('oid', models.AutoField(primary_key=True, serialize=False)),
                ('cust_id', models.PositiveIntegerField()),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.PositiveBigIntegerField()),
                ('address', models.TextField()),
                ('shipping_address', models.BooleanField()),
                ('country', models.CharField(choices=[['India', 'India'], ['USA', 'USA'], ['UK', 'UK']], max_length=30)),
                ('states', models.CharField(choices=[['AP', 'AP'], ['TS', 'TS'], ['SR', 'SR'], ['TN', 'TN']], max_length=30)),
                ('pincode', models.PositiveIntegerField()),
                ('order_date', models.DateTimeField(auto_now=True)),
                ('total_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='order_food_items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_id', models.PositiveIntegerField()),
                ('price', models.FloatField()),
                ('quantity', models.PositiveIntegerField()),
                ('oid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.order_food')),
            ],
        ),
    ]
