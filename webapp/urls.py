from django.urls import re_path
from webapp.views import (
    countries_view,
    database_update,
    )


app_name = 'webapp'
urlpatterns = [
    re_path(r'^update/?$', database_update, name='database_update'),
    re_path(r'^$', countries_view, name='countries'),
    ]
