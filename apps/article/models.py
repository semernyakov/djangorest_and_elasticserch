# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""
Created on 04.04.17
(c) Ivan Semernyakov <direct@beatum-group.ru>
"""

from django.db import models
from django.contrib.postgres.fields import DateTimeRangeField


class Vote(models.Model):
    vote_score = models.IntegerField(default=0)
    vote_up = models.IntegerField(default=0)
    vote_down = models.IntegerField(default=0)

    def __str__(self):  # __unicode__ on Python 2
        return "Like: %d, Dislike: %d, Score: %d" \
            % (self.vote_up, self.vote_down, self.vote_score)

    def save(self, *args, **kwargs):
        self.vote_score = self.calculate_vote_score
        super(Vote, self).save(*args, **kwargs)

    @property
    def calculate_vote_score(self):
        return self.vote_up - self.vote_down


class Article(models.Model):
    title = models.CharField(max_length=255)
    active_range = DateTimeRangeField(blank=True)
    text = models.TextField(blank=True)
    vote = models.ForeignKey(Vote, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):  # __unicode__ on Python 2
        return self.title
