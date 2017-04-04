# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""
Created on 04.04.17
(c) Ivan Semernyakov <direct@beatum-group.ru>
"""

from datetime import timedelta, datetime
from loremipsum import generate_sentence, generate_paragraph
from django.core.management.base import BaseCommand
from apps.article.models import Article


class Command(BaseCommand):
    help = "Shiny new management command."

    def add_arguments(self, parser):
        parser.add_argument('count', nargs=1, type=int)
        print ("La-la-la :) ...")

    def handle(self, *args, **options):
        self.make_article(options)

    def make_article(self, options):
        for _ in xrange(options.get('count')[0]):
            title = generate_sentence()
            text = generate_paragraph()
            active_range = (str(datetime.now()), str(datetime.now() + timedelta(days=3)))
            Article.objects.create(title=title[2], text=text[2], active_range=active_range)
        print ('All done! We have successfully created %d article' % options.get('count')[0])


