from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rontal.views.home', name='home'),
    # url(r'^rontal/', include('rontal.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
) 

# Setting dibawah ini hanya untuk development dan berjalan jika di settings.py 
#   DEBUG=True 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
