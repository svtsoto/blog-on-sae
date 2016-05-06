from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
from mysite import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),
    

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
     url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'blog.views.blog_list', name='blog_list'),
    url(r'^bloglist$', 'blog.views.blog_lists', name='blog_lists'),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATICFILES_DIRS}),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^detail/$', 'blog.views.blog_detail'),
    url(r'^blog/tag/(?P<id>\d+)/$', 'blog.views.blog_filter', name='filtrblog'),
    url(r'^blog/add/$', 'blog_add', name='addblog'),
    (r'^assets/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.ASSETS_DIR}),
    (r'^tinymce/', include('tinymce.urls')),
)

# Serve static files for admin, use this for debug usage only
# `python manage.py collectstatic` is preferred.
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

