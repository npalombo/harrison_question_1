from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'harrison_question_1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'webapp.views.index', name='index'),
    url(r'^state/(?P<state>\w+)/$', 'webapp.views.detail', name='detail'),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^admin/', include(admin.site.urls)),
)
