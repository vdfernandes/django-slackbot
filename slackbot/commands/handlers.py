#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf import settings
from slackbot.models.card import Card
from slackbot.jira.methods import comment_issue
from slackbot.slack.methods import user_info
from slackbot.slack.slackcommand import (
    SlackCommand,
    CmdArgumentParser,
    handle_exceptions
)


class HandleCommand(SlackCommand):

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
                # Validação da existência de card
                card = Card.objects.filter(slack_ts=self.mthread_ts)
                if len(card) == 0:
                    self.text = 'Não tem card, precisa criar.' 
                    self.send()
                else:
                    self.text = 'Tem card, {}'.format(card[0].jira_issue) 
                    self.send()

                # Procesamento da mensagem enviada.
                self.text = 'Processo o que veio na mensagem.' 
                self.send()
                
        except Exception as e:
            text = "\r\n".join([
                "Um erro aconteceu no processamento da mensagem. :{}:".format(
                    settings.REACTION_SAD
                ),
                "*Erro:* `{}`".format(str(e))
            ])        
        self.text = text 
        self.send()