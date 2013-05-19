from django.contrib import admin

from models import (Seed,
                Location,
                Family,
                ScientificName,
                CommonName,
                Variety,
                Germination,
                Supplier,
                SupplierType,
                )

admin.site.register(Seed)
admin.site.register(Location)
admin.site.register(Family)
admin.site.register(ScientificName)
admin.site.register(CommonName)
admin.site.register(Variety)
admin.site.register(Germination)
admin.site.register(Supplier)
admin.site.register(SupplierType)