from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, Inventory

class InitCatalogView(APIView):
    def post(self, request):
        product_info = request.data
        for product_data in product_info:
            product, created = Product.objects.get_or_create(
                product_id=product_data['product_id'],
                defaults={
                    'product_name': product_data['product_name'],
                    'mass_g': product_data['mass_g']
                }
            )
            # Initialize inventory with zero
            Inventory.objects.get_or_create(product=product, defaults={'quantity': 0})

        return Response({"message": "Catalog initialized"}, status=200)


class ProcessRestockView(APIView):
    def post(self, request):
        restock_data = request.data
        for restock in restock_data:
            product = Product.objects.get(product_id=restock['product_id'])
            inventory = Inventory.objects.get(product=product)
            inventory.quantity += restock['quantity']
            inventory.save()

        return Response({"message": "Restock processed"}, status=200)
