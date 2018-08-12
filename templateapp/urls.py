from django.conf.urls import url
from .views import upcoming, ongoing, home

urlpatterns = [
    url(r'^ongoing/$', ongoing),
    url(r'^upcoming/$', upcoming),
    url(r'^code/$', home)
]
