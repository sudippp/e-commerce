# Generated by Django 4.0.5 on 2022-06-20 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_com_app1', '0002_rename_price_product_selling_price_orderplaced'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderplaced',
            name='payment_method',
            field=models.CharField(choices=[('Cash on Delivery', 'Cash on Delivery'), ('UPI Payment', 'UPI Payment'), ('Net Banking', 'Net Banking')], default='Cash on Delivery', max_length=100),
        ),
    ]
