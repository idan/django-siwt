from django.conf.urls.defaults import *

from django_siwt.views import *

urlpatterns = patterns('django_siwt.views',
    url(r'^signin/$',
        view=signin,
        name='siwt_signin'),

    url(r'^callback/$',
        view=callback,
        name='siwt_callback'),
  
    url(r'^signout/$',
        view=signout,
        name='siwt_signout'),
)
