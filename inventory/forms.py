from django import forms
from .models import Stock


class StockForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):                                                        # used to set css classes to the various fields
        super().__init__(*args, **kwargs)
        # self.fields['id'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['grundmaterial'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['artikel'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['artikelnummer'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['artikelbezeichnung'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['fassung'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['besonderheit'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['form'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['farbe'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['zusatzmaterial'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['kette'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['legierung'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['bestand'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['herstellungskosten'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['verkaufspreis'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['hersteller'].widget.attrs.update({'class': 'textinput form-control'})

    class Meta:
        model = Stock
        fields = '__all__'
