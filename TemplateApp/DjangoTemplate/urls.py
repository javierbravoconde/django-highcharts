from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoTemplate.views.home', name='home'),
    # url(r'^DjangoTemplate/', include('DjangoTemplate.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^template/', 'AppTemplate.views.viewtemplate'),
)

urlpatterns += staticfiles_urlpatterns()


