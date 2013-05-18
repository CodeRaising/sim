from django.db import models

# Create your models here.
class Seed(models.Model):
    accession_num = models.CharField(maxlength=8, blank=False)
    lot_num = models.CharField(maxlength=5, blank=False)
    aquisition_date = models.DateField(blank=False)
    cost = models.DecimalField(maxlength=4, blank=False)  

    aquisition_location = models.ForeignKey(Location)
    family = models.ForeignKey(Family)
    variety = models.ForeignKey(Variety)
    scientific_name = models.ForeignKey(ScientificName)
    germination = models.ForeignKey(Germination)

    # I think this one is supposed to be here... ?  
    supplier = models.ForeignKey(Supplier) 

class ScientificName(models.Model):
    scientific_name = models.CharField(maxlength=45, blank=False)

class CommonName(models.Model):
    common_name = models.CharField(maxlength=45)
    langs = (("English", "English"), ("Thai", "Thai"))
    language = models.CharField(maxlength=45, choices=langs, default="English")
    scientific_name = models.ForeignKey(ScientificName)

class Variety(models.Model):
    variety = models.CharField(maxlength=45, blank=False)
    seed_color = models.CharField(maxlength=75)
    parts_to_harvest =  models.TextField()
    unique_characteristics = models.TextField()
    planting_intructions = models.TextField()

    scientific_name = models.ForeignKey(ScientificName)

class Family(models.Model):
    family = models.CharField(maxlength=45, blank=False)

class Location(models.Model):
    location_name = models.CharField(maxlength=45, blank=False)
    location_code = models.CharField(maxlength=45, blank=False)
    location_type = models.CharField(maxlength=45)

class Germination(models.Model):
    germ_rate = models.DecimalField(maxlength=6, blank=False)
    germ_date = models.DateField(blank=False)
    germ_method = models.TextField()

class Supplier(models.Model):
    supplier_name = model.CharField(maxlength=45, blank=False)
    contact_first_name = models.CharField(maxlength=45)
    contact_last_name = models.CharField(maxlength=45)
    contact_phone = models.CharField(maxlength=15)
    contact_email = models.EmailField()
    address_one = models.CharField(maxlength=45, blank=False)
    address_two = models.CharField(maxlength=45)
    city = models.CharField(maxlength=45, blank=False)
    state = models.USStateField()
    zip_code = models.IntegerField(maxlength=10)
    country = models.CharField(maxlength=45, blak=False)
    phone = models.CharField(maxlength=15)
    email = models.EmailField()
    website = models.URLField()

    supplier_type = models.ForeignKey(SupplierTypes)
    primary_seed_bank = models.ForeignKey(Location)
 
class SupplierType(models.Model):
    supplier_type = models.CharField(maxlength=45)
