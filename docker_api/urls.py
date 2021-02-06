from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include

from api import views
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

#---------
router = routers.DefaultRouter()
router.register('Owner', views.OwnerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

]
