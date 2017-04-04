# -*- coding: utf-8 -*-
from __future__ import unicode_literals


"""
Created on 04.04.17
(c) Ivan Semernyakov <direct@beatum-group.ru>
"""

from haystack import indexes
from .models import Article


class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    """Article Inedx"""

    doc = indexes.CharField(document=True, use_template=True)

    title = indexes.CharField(model_attr='title', boost=1.1)
    # Field boosting is enabled by setting the 'boost = 1.125' kwarg
    # on the desired field. 'Title' must have more relevance then 'text'!

    text = indexes.CharField(model_attr='text', boost=0.9)

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
