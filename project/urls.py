# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""
Created on 04.04.17
(c) Ivan Semernyakov <direct@beatum-group.ru>
"""

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from apps.article import viewsets


router = routers.DefaultRouter()
router.register('article', viewsets.ArticleViewSet)
router.register('search', viewsets.ArticleSearchViewSet,
    base_name="search")


urlpatterns = [
    url(r'^', include('haystack.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework'))
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns