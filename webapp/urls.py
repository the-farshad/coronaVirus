from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from webapp.views import (
    countries_view,
    DatabaseUpdate,
    CovidStatisticsAPIView,
    CovidCountryAPIView,
)


app_name = 'webapp'
urlpatterns = [
    re_path(
        r'^update/?$',
        DatabaseUpdate.as_view(),
        name='database_update'
    ),
    re_path(r'^$',countries_view, name='countries'),
    re_path(
        r'^v1/api/covid/?$',
        CovidStatisticsAPIView.as_view(),
        name='covid'
    ),
    re_path(
        r'^v1/api/country/?$',
        CovidCountryAPIView.as_view(),
        name='search'
    ),
    ]


# if settings.DEBUG:
#     urlpatterns += static(
#         settings.MEDIA_URL,
#         document_root=settings.MEDIA_ROOT
#     )
