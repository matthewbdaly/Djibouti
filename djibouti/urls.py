from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from blog.models import Category, Post
from djibouti import settings
from blog.views import PostsFeed
from django.views.generic.base import RedirectView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djibouti.views.home', name='home'),
    # url(r'^djibouti/', include('djibouti.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Favicon
    (r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),

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

    # Category lists
    url(r'^categories/?$', ListView.as_view(
        model=Category,
        )),

    # Individual categories
    url(r'^category/(?P<slug>[a-zA-Z0-9-]+)/?$', 'blog.views.getCategory'),
    url(r'^category/(?P<slug>[a-zA-Z0-9-]+)/?(?P<page>\d+)?/?$', 'blog.views.getCategory'),

    # serve static
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

    # RSS feeds
    url(r'^feeds/posts/$', PostsFeed()),

    # Search posts
    url(r'^search', 'search.views.getSearchResults'),

    # Flat pages
    url(r'', include('django.contrib.flatpages.urls')),
)
