"""admIn URL Configuration

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
from django.urls import include, path
from rest_framework import routers
from quickstart import views

ROUTER = routers.DefaultRouter()
ROUTER.register(r'users', views.UserViewSet)
ROUTER.register(r'groups', views.GroupViewSet)
ROUTER.register(r'permissions', views.PermissionsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(ROUTER.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path(r'snippets', include('snippets.urls'))
]
