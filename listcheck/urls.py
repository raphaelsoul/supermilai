from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fdvworkflow.views.home', name='home'),
    # url(r'^fdvworkflow/', include('fdvworkflow.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^$','listcheck.views.overview'),
    url(r'^handle/page=(.+)$','listcheck.views.overview'),
    url(r'^add_plan.html','listcheck.views.add_plan'),
    url(r'^upload/modify/id=(.+)$','listcheck.views.modify_plan'),
    url(r'^detail/id=(.+)$','listcheck.views.detail_plan'),
    url(r'^modify/id=(.+)$','listcheck.views.modify_plan'),
    url(r'^delete/id=(.+)$','listcheck.views.delete_plan'),
    url(r'^mylistplan/page=(.+)$','listcheck.views.my_listplan'),
    url(r'^ajax/mark_passed.html$','listcheck.views.mark_passed'),
    url(r'^fake_ajax/add_note/id=(.+)$','listcheck.views.add_note'),
    #url(r'^search.html','base.views.search'),
    #url(r'^view_all_containers/page=(.+)$','base.views.all_containers'),
    #url(r'^view_all_items/page=(.+)$','base.views.all_items'),
    #ajax
    #url(r'^ajax/temp_mark.html','base.ajax.temp_mark'),
    #url(r'^ajax/descrption_mark.html','base.ajax.description_mark'),
)
