# Generated by Django 4.x on 2024-10-23

from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShippedProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipment', models.ForeignKey(on_delete=models.CASCADE, to='shipment_service.Shipment')),
                ('product_id', models.IntegerField()),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]