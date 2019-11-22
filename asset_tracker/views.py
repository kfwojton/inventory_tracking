
from django.views.generic import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import *
from django.views import View
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
import os
from django.core.mail import send_mail
from django.contrib import messages
from inventory.models import *
from datetime import *
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class Home(TemplateView):
    template_name = "index.html"

class CreateInventory(CreateView):
    template_name = "createform.html"
    model = Inventory
    fields = ['name','type_of_inventory']
    success_url = 'list_inventory'

class CreateClient(CreateView):
    template_name = "createform.html"
    fields = ['company_name']
    model = Client
    success_url = 'list_clients'

class CreateInvoice(CreateView):
    template_name = "createform.html"
    fields = ['name','type_of_inventory']
    model = Invoice
    success_url = 'list_invoices'

class ListInventory(ListView):
    template_name = "listview.html"
    model = Inventory
    fields = ['company',
            'cost_of_invoice',
            'date_billed']

class ListClients(ListView):
    template_name = "listview.html"
    model = Client

class ListInvoices(ListView):
    template_name = "listview.html"
    model = Invoice
