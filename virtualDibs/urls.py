"""virtualDibs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from user_accounts import views as user_accounts_views
from virtdibs import views
from django.conf.urls import include


urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^dash/$',views.dash,name='dash'),
    url(r'^register/$',user_accounts_views.register,name='register'),
    url(r'^customer_login/',user_accounts_views.customer_login,name='customer_login'),
    url(r'^logout/$', user_accounts_views.user_logout, name='logout'),
    url(r'^password_reset_email/', user_accounts_views.password_reset_email, name='password_reset_email'),
    url(r'^admin/',admin.site.urls),
    url('^',include('django.contrib.auth.urls')),
]
