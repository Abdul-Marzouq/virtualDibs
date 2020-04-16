from django.conf.urls import url
from django.contrib import admin

from boards import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^login_signup/$',views.signupin,name='signupin'),
    url(r'^admin/',admin.site.urls),
]
