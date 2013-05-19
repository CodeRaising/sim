from django import forms
from django.forms.models import inlineformset_factory

from seedbank.models import Seed, Location

# inlineformset_factory creates a Class from a parent model (Seed)
# to a child model (Location)
# SeedLocationFormSet = inlineformset_factory(
#     Seed,
#     Location,
# )


class SeedForm(forms.ModelForm):

    class Meta:
        model = Seed