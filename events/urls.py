# not sure this is being used
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^/all', views.)
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]