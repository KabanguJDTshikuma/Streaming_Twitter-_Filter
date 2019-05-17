from django.shortcuts import render

from .tweeter_folder import tweeter
import tweepy


def filter(request):
    stream_listener = tweeter.StreamListener()
    stream = tweepy.Stream(auth=tweeter.api.auth, listener=stream_listener)
    stream.filter(track=["@djangode", "@django_district", "@reactjs", "@nodejs", "project"])
    return render(request, 'filter/filter.html')
