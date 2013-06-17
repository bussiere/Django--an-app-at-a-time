# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin


# This is required for the admin to work
admin.autodiscover()


urlpatterns = patterns('',

    # this display the admin on the url /admin/
    url(r'^admin/', include(admin.site.urls)),

    # include all our apps, one by one

    # this say that any url starting with 'app1' should be directed to the
    # first app
    url(r'^app1/', include('app1_hello.urls')),

    url(r'^app2/', include('app2_hello_again.urls')),

    # ignore this, it's the page of the project listing all the apps
    url(r'^$', include('ignore_me.urls')),
)
