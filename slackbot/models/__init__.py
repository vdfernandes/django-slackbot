#!/usr/bin/python
# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from django.conf import settings

if settings.DATABASE_ENGINE == 'sqlite':
    dbstring = "sqlite:///{}".format(settings.SQLITE_FILE)
    db = create_engine(dbstring, connect_args={'check_same_thread': False})
else:
    dbstring = "{}+{}://{}:{}@{}:{}/{}".format(
        settings.DATABASE_ENGINE,
        settings.DATABASE_DRIVER,
        settings.DATABASE_USER,
        settings.DATABASE_PASSWORD,
        settings.DATABASE_HOST,
        settings.DATABASE_PORT,
        settings.DATABASE_DATABASE,
    )
    db = create_engine(dbstring)

# Session = sessionmaker(db)
Session = scoped_session(
    sessionmaker(bind=db, autocommit=False, autoflush=False))

# Base = declarative_base()


class _BaseModel(object):
    qry = Session.query_property()
    sess = Session()

    def save(self):
        self.sess.add(self)
        self.sess.commit()

Model = declarative_base(cls=_BaseModel)


def create_all():
    import slackbot.models.card
    import slackbot.models.channel
    print("...Creating models")
    Model.metadata.create_all(db)
    print("...Done")
