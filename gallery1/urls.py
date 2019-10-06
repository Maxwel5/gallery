from django.conf.urls import url
from . import views
# from django.config import settings

urlpatterns=[
    # url('^$',views.home),
    # url('^$',views.home,name = 'home'),
    url('^$',views.create_album,name = 'create_album'),
    url(r'^location/(\d+)',views.location,name='location')
]