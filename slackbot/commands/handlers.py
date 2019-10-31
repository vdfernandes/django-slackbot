#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf import settings
from slackbot.models import Session
from slackbot.models.card import Card
from slackbot.jira.methods import comment_issue
from slackbot.slack.methods import user_info
from slackbot.slack.slackcommand import (
    SlackCommand,
    CmdArgumentParser,
    handle_exceptions
)


class HandleCommand(SlackCommand):
    session = Session()

    @handle_exceptions
    def run(self):
        """
        Método de execução das ações da classe
        """
        try:
            is_thread = True if self.mthread_ts else False
            text = "Testando apenas, eu recebi isso: {}".format(
                str(is_thread)
            )

            if is_thread:
                ####
                self.text = 'Preciso validar se tem card.' 
                self.send()
                ###
                card = self.session.query(Card).filter_by(slack_ts=self.thread_ts).first()
                if card:
                    print('Tem card.')
                
                ###
                self.text = 'Processo o que veio na mensagem.' 
                self.send()
                ###

                ###
                self.text = 'Gravo numa tabela o card.' 
                self.send()
                ###

                ###
                self.text = 'Vou processando as respostas.' 
                self.send()
                ###
        except Exception as e:
            text = "\r\n".join([
                "Um erro aconteceu no processamento da mensagem. :{}:".format(
                    settings.REACTION_SAD
                ),
                "*Erro:* `{}`".format(str(e))
            ])        
        self.text = text 
        self.send()