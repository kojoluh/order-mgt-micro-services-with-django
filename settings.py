# settings.py
INSTALLED_APPS = [
    'rest_framework',  # For APIs
    'channels',        # For asynchronous tasks (Kafka)
    'inventory_service',
    'order_service',
    'shipment_service',
]

# Kafka settings (can be added to environment variables)
KAFKA_BROKER_URL = "localhost:9092"

# ASGI Application
ASGI_APPLICATION = 'order_service.asgi.application'

# Channels Layer
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
    },
}
