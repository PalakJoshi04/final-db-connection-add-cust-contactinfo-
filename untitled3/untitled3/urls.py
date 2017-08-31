from django.conf.urls import url
from sample3.views import people, index

from django.contrib import admin
admin.autodiscover()

urlpatterns = (
    url(r'^admin/', admin.site.urls),
    url(r'^people$', people, name='people'),
    url(r'^$', index, name='index'),

)