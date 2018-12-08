"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from django.views.generic.base import RedirectView


from .apps.products import api

router = routers.DefaultRouter()
router.register(r'products', api.ProductApi, base_name="product")


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/', include((router.urls, 'store'), namespace='rest_framework')),
    re_path(r'^api/', include(router.urls)),
    re_path(r'^.*$', RedirectView.as_view(url='http://localhost:8000/api', permanent=False), name='index')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
