from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Countries


# Create your views here.
def countries_view(request):
    # list of countries show in page
    queryset = Countries.object.all()
    context = {
        'object_list' = queryset,
    }

