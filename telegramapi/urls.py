from django.urls import re_path
from telegramapi.views import (
    kurdistan_statistics,
)


app_name = 'telegrampapi'
urlpatterns = [
    re_path(r'^kurditan/?$', kurdistan_statistics, name='kurdistan_statistics'),
]
