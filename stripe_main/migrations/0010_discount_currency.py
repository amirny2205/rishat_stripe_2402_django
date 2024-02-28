# Generated by Django 5.0.2 on 2024-02-27 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stripe_main', '0009_tax_currency_alter_order_discount_alter_order_items_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='currency',
            field=models.CharField(choices=[('usd', 'usd'), ('rur', 'rur')], default='usd'),
            preserve_default=False,
        ),
    ]