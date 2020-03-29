from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
User = settings.AUTH_USER_MODEL

class Scores(models.Model):
	Owner= models.ForeignKey(User,on_delete=models.CASCADE,default=1)
	created=models.DateField(auto_now_add=True)	
	updated=models.DateField(auto_now=True)	
	score=models.IntegerField(default=0)
    
	def __str__(self):
		return str(self.Owner)
