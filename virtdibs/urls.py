from django.urls import path
from virtdibs import views

urlpatterns = {
path('',views.index,name='index'),
}
