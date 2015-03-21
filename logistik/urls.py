from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'logistik.views.home', name='home'),
    # url(r'^logistik/', include('logistik.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^index.html','logistik.views.overview'),
    url(r'^$','logistik.views.overview'),
    url(r'^add_container.html','logistik.views.add_container'),
    url(r'^container/modify/id=(.+)$','logistik.views.modify_container'),
    url(r'^container/detail/id=(.+)$','logistik.views.detail_container'),
    url(r'^search.html','logistik.views.search'),
    url(r'^view_all_containers/page=(.+)$','logistik.views.all_containers'),
    url(r'^view_all_items/page=(.+)$','logistik.views.all_items'),
    #ajax
    url(r'^ajax/temp_mark.html','logistik.ajax.temp_mark'),
    url(r'^ajax/descrption_mark.html','logistik.ajax.description_mark'),
    url(r'^ajax/lots_size_mark.html$','logistik.ajax.lot_size_mark'),
)
