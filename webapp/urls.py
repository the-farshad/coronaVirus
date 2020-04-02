from django.urls import path
from webapp.views import (
        home_view,
        )

app_name = 'webapp'
urlpatterns=[
        path('', home_view, name='home'),
        ]
