from django.urls import path,re_path
from Trains_Info import views

urlpatterns = [
    re_path(r'^$',views.home,name='home'),
    re_path(r'^train_info',views.train_info,name='train_info'),
    re_path(r'^report',views.report,name='report')
]