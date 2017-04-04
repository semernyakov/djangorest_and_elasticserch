# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""
Created on 04.04.17
(c) Ivan Semernyakov <direct@beatum-group.ru>
"""

from rest_framework import viewsets
from drf_haystack.viewsets import HaystackViewSet
from drf_haystack.filters import HaystackFilter
from drf_haystack.filters import HaystackHighlightFilter
from drf_haystack.filters import HaystackBoostFilter
from .serializers import ArticleSerializer
from .serializers import ArticleHaystackSerializer
from .utils import active_range_filter
from .models import Article


class ArticleViewSet(viewsets.ModelViewSet):
    """Article View Set"""

    queryset = Article.objects.filter(
        id__in=[obj.id for obj in active_range_filter()])
    # Append active range filter results to queryset
    
    serializer_class = ArticleSerializer


class ArticleSearchViewSet(HaystackViewSet):
    """Article Search View Set"""
    index_models = [Article]
    serializer_class = ArticleHaystackSerializer
    filter_backends = [HaystackFilter, HaystackBoostFilter,
                       HaystackHighlightFilter]
