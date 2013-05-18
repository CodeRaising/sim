from django.db import models

# Create your models here.
class Seed(models.Model):
    accession_num = models.CharField(max_length=8, blank=False)
    lot_num = models.CharField(max_length=5, blank=False)
    aquisition_date = models.DateField(blank=False)
    cost = models.DecimalField(max_length=4, blank=False)  

    aquisition_location = models.ForeignKey(Location)
    family = models.ForeignKey(Family)
    variety = models.ForeignKey(Variety)
    scientific_name = models.ForeignKey(ScientificName)
    germination = models.ForeignKey(Germination)

    # I think this one is supposed to be here... ?  
    supplier = models.ForeignKey(Supplier) 

class ScientificName(models.Model):
    scientific_name = models.CharField(max_length=45, blank=False)

class CommonName(models.Model):
    common_name = models.CharField(max_length=45)
    langs = (("English", "English"), ("Thai", "Thai"))
    language = models.CharField(max_length=45, choices=langs, default="English")
    scientific_name = models.ForeignKey(ScientificName)

class Variety(models.Model):
    variety = models.CharField(max_length=45, blank=False)
    seed_color = models.CharField(max_length=75)
    parts_to_harvest =  models.TextField()
    unique_characteristics = models.TextField()
    planting_intructions = models.TextField()

    scientific_name = models.ForeignKey(ScientificName)

class Family(models.Model):
    family = models.CharField(max_length=45, blank=False)

class Location(models.Model):
    location_name = models.CharField(max_length=45, blank=False)
    location_code = models.CharField(max_length=45, blank=False)
    location_type = models.CharField(max_length=45)

class Germination(models.Model):
    germ_rate = models.DecimalField(max_length=6, blank=False)
    germ_date = models.DateField(blank=False)
    germ_method = models.TextField()

class Supplier(models.Model):
    supplier_name = model.CharField(max_length=45, blank=False)
    contact_first_name = models.CharField(max_length=45)
    contact_last_name = models.CharField(max_length=45)
    contact_phone = models.CharField(max_length=15)
    contact_email = models.EmailField()
    address_one = models.CharField(max_length=45, blank=False)
    address_two = models.CharField(max_length=45)
    city = models.CharField(max_length=45, blank=False)
    state = models.USStateField()
    zip_code = models.IntegerField(max_length=10)
    country = models.CharField(max_length=45, blank=False)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    website = models.URLField()

    supplier_type = models.ForeignKey(SupplierTypes)
    primary_seed_bank = models.ForeignKey(Location)
 
class SupplierType(models.Model):
    supplier_type = models.CharField(max_length=45)
