# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""
Created on 04.04.17
(c) Ivan Semernyakov <direct@beatum-group.ru>
"""

from rest_framework import serializers
from drf_haystack.serializers import HaystackSerializer
from drf_haystack.serializers import HighlighterMixin
from .search_indexes import ArticleIndex
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    """Article Default Serializer"""
    class Meta:
        model = Article
        fields = '__all__'


class ArticleHaystackSerializer(HighlighterMixin, HaystackSerializer):
    """Article Haystack Serializer"""

    highlighter_css_class = "highlighted"
    highlighter_html_tag = "span"

    class Meta:
        index_classes = [ArticleIndex]
        fields = ["title", "text"]
