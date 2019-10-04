from django.conf.urls import url
from . import views

urlpatterns=[
    # url(r'^admin/'.admin.site.urls),
    url('^$',views.home),
    # url('^$',views.home,name = 'home'),
    url('^$',views.create_album,name = 'create_album'),
]