from django.conf.urls import patterns, url

from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', 'video.views.home', {'template_name': 'video/text.html'}, name='video-home'),
    #url(r'^picture/', TemplateView.as_view(template_name='video/index.html'), name='video-picture'),
    #url(r'^photo/', TemplateView.as_view(template_name='video/photo.html'), name='video-photo'),
    url(r'^text$', 'video.views.home', {'template_name': 'video/text.html'}, name='video-text'),
    url(r'^video$', 'video.views.home', {'template_name': 'video/video.html'}, name='video'),
    url(r'^index$', 'video.views.home', {'template_name': 'video/index2.html'}, name='video-index'),
    url(r'^node_api$', 'video.views.node_api', name='node_api'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'admin/login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    url(r'^conference/$', TemplateView.as_view(template_name='video/conference.html'), name='video-conference' ),
)