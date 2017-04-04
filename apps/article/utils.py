# -*- coding: utf-8 -*-
from __future__ import unicode_literals


"""
Created on 04.04.17
(c) Ivan Semernyakov <direct@beatum-group.ru>
"""

from django.utils import timezone
from django.shortcuts import get_list_or_404
from .models import Article


def active_range_filter():
    """
    Active range filter - This method returns a list with the current items
    filtered by the upper border of the DateTimeTZRange field
    :return: object_list
    """
    queryset = get_list_or_404(Article, active_range__isempty=False)
    objects_list = []
    for i in queryset:
        if i.active_range.upper >= timezone.now():
            objects_list.append(i)
    return objects_list
