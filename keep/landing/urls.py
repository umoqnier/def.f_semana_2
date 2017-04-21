from django.conf.urls import url, include
from .views import index, agregar

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^agregar/$', agregar, name="agregar"),
]