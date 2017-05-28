"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from apps.domochat import views


urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'company/(?P<name>.+(\s+?.+?)?)/', views.index_view, name='index'),

    url(r'company/orders/$', views.order_list_view, name='orders'),
    url(r'company/orders/(?P<order_id>\d)/$', views.order_item_view, name='show_order'),



]
