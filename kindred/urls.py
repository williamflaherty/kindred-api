from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kindred.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^kindred_api/', include('kindred_api.urls', namespace='kindred_api')),
    url(r'^$', include('kindred_api.urls', namespace='kindred_api')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
