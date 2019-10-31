#!/usr/bin/python
# -*- coding: utf-8 -*-
from jira import JIRA
from django.conf import settings

# JIRA Credentials
user = settings.JIRA_USER
passwd = settings.JIRA_PASSWORD
server = settings.JIRA_SERVER

# JIRA Client
client = JIRA(
    server=server,
    basic_auth=(
        user,
        passwd
    )
)
