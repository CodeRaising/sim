from django.db import models

# Create your models here.

class Location(models.Model):
    """
    TODO: Description of class
    """
    location_name = models.CharField(max_length=45, blank=False)
    location_code = models.CharField(max_length=45, blank=False)
    location_type = models.CharField(max_length=45)


class Family(models.Model):
    """
    TODO: Description of class
    """
    family = models.CharField(max_length=45, blank=False)


class ScientificName(models.Model):
    """
    TODO: Description of class
    """
    scientific_name = models.CharField(max_length=45, blank=False)


class Variety(models.Model):
    """
    TODO: Description of class
    """
    variety = models.CharField(max_length=45, blank=False)
    seed_color = models.CharField(max_length=75)
    parts_to_harvest = models.TextField()
    unique_characteristics = models.TextField()
    planting_intructions = models.TextField()

    scientific_name = models.ForeignKey(ScientificName)


class Germination(models.Model):
    """
    TODO: Description of class
    """
    germ_rate = models.DecimalField(decimal_places=2, max_digits=2, blank=False)
    germ_date = models.DateField(blank=False)
    germ_method = models.TextField()


class CommonName(models.Model):
    """
    TODO: Description of class
    """
    common_name = models.CharField(max_length=45)
    langs = (("English", "English"), ("Thai", "Thai"))
    language = models.CharField(max_length=45, choices=langs, default="English")
    scientific_name = models.ForeignKey(ScientificName)


class SupplierType(models.Model):
    """
    TODO: Description of class
    """
    supplier_type = models.CharField(max_length=45)


class Supplier(models.Model):
    """
    TODO: Description of class
    """
    supplier_name = models.CharField(max_length=45, blank=False)
    contact_first_name = models.CharField(max_length=45)
    contact_last_name = models.CharField(max_length=45)
    contact_phone = models.CharField(max_length=15)
    contact_email = models.EmailField()
    address_one = models.CharField(max_length=255, blank=False)
    address_two = models.CharField(max_length=255)
    city = models.CharField(max_length=255, blank=False)
    state = models.CharField(max_length=45)
    zip_code = models.IntegerField(max_length=10)
    country = models.CharField(max_length=45, blank=False)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    website = models.URLField()

    supplier_type = models.ForeignKey(SupplierType)
    primary_seed_bank = models.ForeignKey(Location)


class Seed(models.Model):
    """
    TODO: Description of class
    """
    accession_num = models.CharField(max_length=8, blank=False)
    lot_num = models.CharField(max_length=5, blank=False)
    aquisition_date = models.DateField(blank=False)
    cost = models.DecimalField(decimal_places=2, max_digits=6, blank=False)

    aquisition_location = models.ForeignKey(Location)
    family = models.ForeignKey(Family)
    variety = models.ForeignKey(Variety)
    scientific_name = models.ForeignKey(ScientificName)
    germination = models.ForeignKey(Germination)

    # I think this one is supposed to be here... ?
    supplier = models.ForeignKey(Supplier)

    def get_absolute_url(self):
        return reverse('seeds-view', kwargs={'pk': self.id})
