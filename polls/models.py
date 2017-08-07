# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



class Question(models.Model):
	question_text=models.CharField(max_length=1000)
	pub_date=models.DateTimeField()
	
	def __str__(self):
		return self.question_text+" published on "+ str(self.pub_date)

class Choice(models.Model):
	question=models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text=models.CharField(max_length=3000)
	votes=models.IntegerField(default=0)
	
	def __str__(self):
		return self.choice_text +" "+str(self.votes)

