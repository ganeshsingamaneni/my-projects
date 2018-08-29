from django.db import models

# Create your models here.
from mongoengine import *
import mongoengine
mongoengine.connect('test','mongodb://ganesh:ganesh55@localhost:27017')


class ChoiceModel(EmbeddedDocument):
    choice_text = StringField(max_length=200)
    votes = IntField(default=0)


class PollModel(Document):
    question = StringField(max_length=200)
    pub_date = DateTimeField(help_text='date published')
    choices = ListField(EmbeddedDocumentField(ChoiceModel))
