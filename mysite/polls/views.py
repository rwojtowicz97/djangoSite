from django.http import HttpResponse, response
from django.shortcuts import render
from .models import Question
from django.template import context, loader

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse("You are looking at question%s." %question_id)

def results(request, question_id):
    response = "Youe are looking at the result of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s." % question_id)