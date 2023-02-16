# Generated by Django 4.1.6 on 2023-02-16 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_product_id_alter_variation_id'),
        ('orders', '0002_alter_order_is_ordered_alter_order_order_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='color',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='size',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='variation',
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='variations',
            field=models.ManyToManyField(blank=True, to='store.variation'),
        ),
    ]