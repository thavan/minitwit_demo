from django.db import models
from django.contrib.auth.models import User


class Tweet(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	message = models.CharField(max_length=300)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.author.username + ' - ' + self.message[:50]