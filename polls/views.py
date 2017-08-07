from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Question

def index(request):
	all_quest=Question.objects.all()
	return render(request,'polls/index.html',{'all_q':all_quest})

def detail(request,question_id):
	quest=get_object_or_404(Question,pk=question_id)
	return render(request,'polls/detail.html',{'quest':quest})
