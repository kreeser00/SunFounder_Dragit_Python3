"""picar_v_snap URL Configuration

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
from django.urls import path
from django.contrib import admin
from picar_v import views as picar_v_views
from raspberry_pi import views as raspberry_pi_views
from picar_s import views as picar_s_views
from pismart_ import views as pismart_views
from modules import views as modules_views
from piplus import views as piplus_views
from views import home, SnapCloud

urlpatterns = [
    path(r'^admin/', admin.site.urls),
    path(r'^$', home),
    path(r'^SnapCloud$', SnapCloud),
    path(r'^SnapCloudSignUp/$', SnapCloud),
    path(r'^run/picar-v/$', picar_v_views.run),
    path(r'^run/raspberry_pi/$', raspberry_pi_views.run),
    path(r'^run/picar-s/$', picar_s_views.run),
    path(r'^run/pismart/$', pismart_views.run),
    path(r'^run/modules/$', modules_views.run),
    path(r'^run/piplus/$', piplus_views.run),
]
