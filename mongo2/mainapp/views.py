# Create your views here.
from mainapp.models import PollModel, ChoiceModel
import datetime
from django.shortcuts import render
from django.http import HttpResponse
import mongoengine
from mongoengine import *
connect("test")

def create(request):

    choice1 = ChoiceModel(choice_text="option a", votes=20)
    choice2 = ChoiceModel(choice_text="option a", votes=12)
    choice3 = ChoiceModel(choice_text="option a", votes=9)
    choice4 = ChoiceModel(choice_text="option a", votes=21)

    choices = [choice1, choice2, choice3, choice4]

    poll = PollModel(question="This is a sample question", pub_date=datetime.datetime.now(), choices=choices)
    poll.save()

    poll = PollModel(question="This is another sample question with same choices", pub_date=datetime.datetime.now(),
                     choices=choices)
    poll.save()

    return HttpResponse("save")


def show(request):
    data = {}
    p = PollModel.objects.all()
    data["polls"] = p
    return render(request, "index.html", data)
