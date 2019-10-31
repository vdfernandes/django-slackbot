#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models


class Card(models.Model):
    class Meta:
        app_label = 'slackbot'

    slack_ts = models.CharField(unique=True, max_length=30, primary_key=True)
    jira_issue = models.CharField(unique=True, max_length=30)
    status = models.CharField(max_length=20)
    channel = models.CharField(max_length=100)
    requester = models.CharField(max_length=100)
    executor = models.CharField(max_length=100)

    def __str__(self):
        return "Slack TS: {}, Issue: {}".format(
            self.slack_ts,
            self.jira_issue
        )    
