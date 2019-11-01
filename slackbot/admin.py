#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib import admin
from slackbot.models.card import Card
from slackbot.models.channel import Channel

# Instanciando models para o Admin
admin.site.register(Card)
admin.site.register(Channel)