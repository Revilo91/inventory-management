from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    View,
    CreateView,
    UpdateView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Stock
from .forms import StockForm
from django_filters.views import FilterView
from .filters import StockFilter


class StockListView(FilterView):
    filterset_class = StockFilter
    queryset = Stock.objects.all()
    template_name = 'inventory.html'
    paginate_by = 10


class StockCreateView(SuccessMessageMixin, CreateView):                                 # createview class to add new stock, mixin used to display message
    model = Stock                                                                       # setting 'Stock' model as model
    form_class = StockForm                                                              # setting 'StockForm' form as form
    template_name = "edit_stock.html"                                                   # 'edit_stock.html' used as the template
    success_url = '/inventory'                                                          # redirects to 'inventory' page in the url after submitting the form
    success_message = "Produkt erfolgreich angelegt"                                    # displays message when form is submitted

    def get_context_data(self, **kwargs):                                               # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'Neues Produkt'
        context["savebtn"] = 'Hinzufügen'
        return context


class StockUpdateView(SuccessMessageMixin, UpdateView):                                 # updateview class to edit stock, mixin used to display message
    model = Stock                                                                       # setting 'Stock' model as model
    form_class = StockForm                                                              # setting 'StockForm' form as form
    template_name = "edit_stock.html"                                                   # 'edit_stock.html' used as the template
    success_url = '/inventory'                                                          # redirects to 'inventory' page in the url after submitting the form
    success_message = "Produkt erfolgreich bearbeitet"                                  # displays message when form is submitted

    def get_context_data(self, **kwargs):                                               # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'Produkt bearbeiten'
        context["savebtn"] = 'Update'
        context["delbtn"] = 'Löschen'
        return context


class StockDeleteView(View):                                                            # view class to delete stock
    template_name = "delete_stock.html"                                                 # 'delete_stock.html' used as the template
    success_message = "Stock has been deleted successfully"                             # displays message when form is submitted

    def get(self, request, pk):
        stock = get_object_or_404(Stock, pk=pk)
        return render(request, self.template_name, {'object' : stock})

    def post(self, request, pk):
        PK = {'Beton': 'B', 'Harz': 'H', 'Leder': 'L', 'Perlen': 'P', 'Makramee': 'M', 'Phiole': 'I', 'Kordel': 'K', 'Fimo': 'F', 'Holz': 'O', 'Alkoholtinte': 'A', 'Naturstein': 'N', 'Edelstahl': 'E', 'Papier': 'J'}
        stock = get_object_or_404(Stock, pk=pk)
        stock["ID"] = f"{stock['Hersteller'][0]}-{PK[stock['Grundmaterial']]}-{stock['Artikel'][0]}-{stock['Artikelnummer']}"
        stock.save()
        messages.success(request, self.success_message)
        return redirect('inventory')