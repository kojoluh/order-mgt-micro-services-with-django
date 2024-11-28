from kafka import KafkaConsumer
from .models import Shipment, ShipmentItem
import json

consumer = KafkaConsumer(
    'shipment_topic',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

def process_shipment_event():
    """
    Listen for shipment events and ship packages.
    """
    for message in consumer:
        shipment_data = message.value
        order_id = shipment_data['order_id']
        shipped_items = shipment_data['shipped']
        ship_package(order_id, shipped_items)


def ship_package(order_id, shipped_items):
    shipment = Shipment.objects.create(order_id=order_id)
    for item in shipped_items:
        ShipmentItem.objects.create(shipment=shipment, product_id=item['product_id'], quantity=item['quantity'])
    print(f"Order {order_id}: Shipping {shipped_items}")

