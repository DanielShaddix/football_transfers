from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Question


def indexpolls(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detali(request, question_id):
    return HttpResponse("You're looking at questin %s." %question_id)

def results(request, question_id):
    response = "You're looking at hte result  of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def index0(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)



# def index0(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = RequestContext(request, {
#         'latest_question_list': latest_question_list,
#     })
#     return HttpResponse(template.render(context))

# Create your views here.
