from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout

#from Binding.views import hello, current_datetime, hours_ahead
from Binding.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Binding.views.home', name='home'),
    # url(r'^Binding/', include('Binding.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    #(r'^hello/$', hello),
    (r'^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    (r'^hello_base/$', hello_base),
    (r'^request_test/$', request_test),
    url(r'^UsersSearch/$', 'Binding.Users.views.search_form'),
    url(r'^search1/$', 'Binding.Users.views.search1'),
    url(r'^search/$', 'Binding.Users.views.search'),
    url(r'^ClassRoom/add/$', 'person.views.classroom_add'),
    url(r'^ClassRoom/list/$', 'person.views.classroom_list'),
    url(r'^ClassRoom/modify/(\d+)/$', 'person.views.classroom_modify'),
    url(r'^ClassRoom/delete/(\d+)/$', 'person.views.classroom_delete'),
    url(r'^view_pic/$', 'Binding.views.my_image'),
    url(r'^test_pdf/$', 'Binding.views.hello_pdf'),
    url(r'^test_cookie/show/$', 'Binding.views.show_cookie'),
    url(r'^test_cookie/set/(\w+)/$', 'Binding.views.set_cookie'),
    url(r'^test_cookie/del/$', 'Binding.views.del_cookie'),
    url(r'^test_session/show/$', 'Binding.views.show_session'),
    url(r'^test_session/set/(\w+)/$', 'Binding.views.set_session'),
    url(r'^test_session/del/$', 'Binding.views.del_session'),
    #url(r'^accounts/login/$',  login),
    url(r'^accounts/login/$',  login, {'template_name': 'login.html'}),
    url(r'^accounts/logout/$', logout, {'template_name': 'login.html'}),
    url(r'^welcome/$', 'Binding.views.welcome'),

    url(r'^user/add/$', 'Binding.user.views.create_user'),
    url(r'^user/list/$', 'Binding.user.views.user_list'),
    url(r'^user/modify/(\d+)/$', 'Binding.user.views.user_modify'),
    url(r'^user/delete/(\d+)/$', 'Binding.user.views.user_delete'),

)
