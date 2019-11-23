
from django.conf.urls.defaults import patterns, url
from django.views.generic import DetailView, TemplateView
urlpatterns = patterns('myproject.geo.views',
    
        # url(r'^$', indexes),
    # url(r'^login/$', indexes),
        url(r'^analysis/$', 'geotech'),
        url(r'^bearingcapacity/$', 'bch'),
         url(r'^endbearingcapacity/$', 'ech'),
         url(r'^skincapacity/$', 'sc'),
         url(r'^settlement/$', 's'),



    )
