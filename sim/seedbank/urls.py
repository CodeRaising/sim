# Django
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# Ours
from .views import SeedCreateView, SeedUpdateView, SeedDeleteView, SeedDetailView, SeedListView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html')),

    #########
    # SEEDS #
    #########
    # For an explanation of how this works, see: https://github.com/CodeRaising/sim/wiki/URL-Scheme#seeds
    # Create a new seed (lot)
    url(r'^seeds/add/$', view=SeedCreateView.as_view(), name='create-seed'),  # TODO: map this to something that has subclassed ListView

    # Edit an existing seed
    url(r'^seeds/edit/$', view=SeedUpdateView.as_view(), name='edit-seed'),  # TODO: map this to something that has subclassed UpdateView

    # Detail view for one seed
    url(r'^seeds/\w+/(?P<id>\d+)/', view=SeedDetailView.as_view(), name='seed-detail'),  # TODO: map this to a class that has subclassed DetailView

    # Delete a given seed
    url(r'^seeds/\w+/delete/(?P<id>\d+)/', view=SeedDeleteView.as_view(), name='delete-seed',),  # delete

    # List all the seeds
    url(r'^seeds/$', view=SeedListView.as_view(), name='seeds_list'),  # TODO: map this to something that has subclassed ListView

    ####################
    # SCIENTIFIC NAMES #
    ####################
)
