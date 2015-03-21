from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'supermilai.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'supermilai.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('account.urls')),
    url(r'^autotemplate/', include('autotemplate.urls')),
    url(r'^logistik/', include('logistik.urls')),
    url(r'^workflow/', include('workflow.urls')),
    url(r'^listcheck/', include('listcheck.urls')),
    url(r'^static/(?P<path>.*)', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    url(r'^django-version$', 'supermilai.views.django_version', name='index'),
)