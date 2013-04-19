from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'chat.views.home', {'template_name': 'chat/text.html'}, name='home'),
    url(r'^text$', 'chat.views.home', {'template_name': 'chat/text.html'}, name='home'),
    url(r'^video$', 'chat.views.home', {'template_name': 'chat/video.html'}, name='home'),
    url(r'^index$', 'chat.views.home', {'template_name': 'chat/index2.html'}, name='home'),
    url(r'^node_api$', 'chat.views.node_api', name='node_api'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'admin/login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
)
