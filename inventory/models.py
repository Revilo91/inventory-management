from django.db import models
# from compositekey import db


class Stock(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=20)  # Field name made lowercase.
    grundmaterial = models.CharField(db_column='Grundmaterial', max_length=50)  # Field name made lowercase.
    artikel = models.CharField(db_column='Artikel', max_length=50)  # Field name made lowercase.
    artikelnummer = models.IntegerField(db_column='Artikelnummer')  # Field name made lowercase.
    artikelbezeichnung = models.CharField(db_column='Artikelbezeichnung', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fassung = models.CharField(db_column='Fassung', max_length=50, blank=True, null=True)  # Field name made lowercase.
    besonderheit = models.CharField(db_column='Besonderheit', max_length=50, blank=True, null=True)  # Field name made lowercase.
    form = models.CharField(db_column='Form', max_length=50, blank=True, null=True)  # Field name made lowercase.
    farbe = models.CharField(db_column='Farbe', max_length=50, blank=True, null=True)  # Field name made lowercase.
    zusatzmaterial = models.CharField(db_column='Zusatzmaterial', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kette = models.CharField(db_column='Kette', max_length=50, blank=True, null=True)  # Field name made lowercase.
    legierung = models.CharField(db_column='Legierung', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bestand = models.IntegerField(db_column='Bestand', blank=True, null=True)  # Field name made lowercase.
    herstellungskosten = models.DecimalField(db_column='Herstellungskosten', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    verkaufspreis = models.DecimalField(db_column='Verkaufspreis', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    hersteller = models.CharField(db_column='Hersteller', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Lagerliste'

