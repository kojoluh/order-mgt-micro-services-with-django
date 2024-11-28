from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Order, OrderItem
from .kafka_client import send_order_created_event

class ProcessOrderView(APIView):
    def post(self, request):
        order_data = request.data
        order = Order.objects.create()
        
        # Create order items
        for item in order_data['requested']:
            OrderItem.objects.create(order=order, product_id=item['product_id'], quantity=item['quantity'])
        # Send the order event to Kafka
        send_order_created_event(order)
        return Response({"message": "Order processed", "order_id": order.order_id}, status=200)
