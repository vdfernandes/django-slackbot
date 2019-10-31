#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models


class Channel(models.Model):
    class Meta:
        app_label = 'slackbot'

    channel = models.CharField(unique=True, max_length=30, primary_key=True)
    project = models.CharField(unique=True, max_length=10)
    issuetype = models.CharField(max_length=10)
    priority = models.CharField(max_length=20)
    id_tr_close = models.IntegerField(blank=True, null=True)
    id_tr_reopen = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "Channel: {}, Project: {}".format(
            self.channel,
            self.project
        )    