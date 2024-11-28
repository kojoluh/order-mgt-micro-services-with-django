# Generated by Django 4.2.5 on 2024-10-23 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shipment_service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShipmentItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='shipment',
            old_name='created_at',
            new_name='shipped_at',
        ),
        migrations.AlterField(
            model_name='shipment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.DeleteModel(
            name='ShippedProduct',
        ),
        migrations.AddField(
            model_name='shipmentitem',
            name='shipment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='shipment_service.shipment'),
        ),
    ]