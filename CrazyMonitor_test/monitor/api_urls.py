

from django.conf.urls import url

import views

urlpatterns = [

    url(r'client/config/(\d+)/$',views.client_configs ),
    url(r'client/service/report/$',views.service_data_report ),
    url(r'hosts/status/$',views.hosts_status,name='get_hosts_status' )

]
