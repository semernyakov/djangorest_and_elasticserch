# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""
Created on 04.04.17
(c) Ivan Semernyakov <direct@beatum-group.ru>
"""

from django import forms
from django.contrib.postgres.forms.ranges import BaseRangeField
from django.contrib.admin.widgets import AdminSplitDateTime
from psycopg2.extras import DateTimeTZRange


class CustomDateTimeField(forms.SplitDateTimeField):
    widget = AdminSplitDateTime


class CustomDateTimeRangeField(BaseRangeField):
    default_error_messages = {'invalid': u'Enter two valid date/times.'}
    base_field = CustomDateTimeField
    range_type = DateTimeTZRange
