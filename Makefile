####################################################################################################
# Default 
####################################################################################################
clean-pyc:
	@find . -name '*.pyc' -exec rm --force {} +
	@find . -name '*.pyo' -exec rm --force {} +
	@find . -name '*~' -exec rm --force  {} +

####################################################################################################
# Django 
####################################################################################################
install:
	pip3 install -r requirements.txt

shell:
	@python3 manage.py shell

run:
	@python3 manage.py runserver

####################################################################################################
# Slack 
####################################################################################################
find-user-id:
	@python3 -c "from slackbot.slack.methods import find_id; print(find_id('user','$(USER)'))"

find-channel-id:
	@python3 -c "from slackbot.slack.methods import find_id; print(find_id('channel','$(CHANNEL)'))"

find-pchannel-id:
	@python3 -c "from slackbot.slack.methods import find_id; print(find_id('priv_channel','$(CHANNEL)'))"
