from django.shortcuts import render

from .models import Tweet

def home(request):
	tweets = Tweet.objects.all()
	return render(request, 'home.html', { # context
			'tweets': tweets
		})