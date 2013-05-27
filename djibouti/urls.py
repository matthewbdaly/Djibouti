from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from blog.models import Post

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djibouti.views.home', name='home'),
    # url(r'^djibouti/', include('djibouti.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Blog post lists
    url(r'^(?P<page>\d+)?/?$', ListView.as_view(
        model=Post,
        paginate_by=5,
        )),

    # Individual vacancies
    url(r'^(?P<pub_date__year>\d{4})/(?P<pub_date__month>\d{1,2})/(?P<slug>[a-zA-Z0-9-]+)/?$', DetailView.as_view(
        model=Post,
        )),

    # Flat pages
    url(r'', include('django.contrib.flatpages.urls')),
)
