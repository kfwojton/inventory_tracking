"""asset_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from asset_tracker.views import *

urlpatterns = [
    path('', Home.as_view()),
    path('admin/', admin.site.urls),
    path('create_inventory', CreateInventory.as_view()),
    path('create_client', CreateClient.as_view()),
    path('create_invoice', CreateInvoice.as_view()),
    path('list_inventory',ListInventory.as_view()),
    path('list_clients', ListClients.as_view()),
    path('list_invoices', ListInvoices.as_view()),



]
