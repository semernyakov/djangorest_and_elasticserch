# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""
Created on 04.04.17
(c) Ivan Semernyakov <direct@beatum-group.ru>
"""

from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Article, Vote
from .widgets import CustomDateTimeRangeField


class ArticleAdminForm(forms.ModelForm):
    active_range = CustomDateTimeRangeField()

    class Meta:
        model = Article
        fields = ['id', 'title', 'vote', 'active_range', 'text']


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'vote_up', 'vote_down', 'vote_score']
    list_editable = ('vote_up', 'vote_down')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm
    list_display = ['id', 'title', 'view_vote']
    list_display_links = list_display
    save_as = True

    def view_vote(self, obj):
        if obj.vote:
            return "Like: %d, Dislike: %d, Score: %d" \
                % (obj.vote.vote_up, obj.vote.vote_down, obj.vote.vote_score)


    view_vote.short_description = 'vote'
    view_vote.empty_value_display = '--empty--'


admin.site.unregister(Group)

