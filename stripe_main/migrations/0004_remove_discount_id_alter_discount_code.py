# Generated by Django 5.0.2 on 2024-02-29 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stripe_main', '0003_alter_discount_table_alter_item_table_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discount',
            name='id',
        ),
        migrations.AlterField(
            model_name='discount',
            name='code',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]