from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views
import events.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^events/', include('events.urls')),
    url(r'^$', events.views.index, name='index'),
    url(r'^contact/', events.views.contact, name='contact'),
    url(r'^recurring/', events.views.recurring, name='recurring'),
    # url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
]
