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
    url(r'^all_tasks/page=(.+)$','workflow.views.all_tasks'),
    url(r'^handle_task_asign.html$','workflow.views.handle_tasks_asign'),
    url(r'^my_tasks.html$','workflow.views.my_tasks'),
    #url(r'^container/modify/id=(.+)$','logistik.views.modify_container'),
    #ajax
)
