"""
URL configuration for inventory_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import InitCatalogView, ProcessRestockView

urlpatterns = [
    path('inventory_service/api/init_catalog/', InitCatalogView.as_view(), name='init_catalog'),
    path('inventory_service/api/process_restock/', ProcessRestockView.as_view(), name='process_restock'),
]
