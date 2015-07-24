import datetime 
from kindred_api import models
from kindred_api.serializers import *
# TODO: why are serializers in here?
from django.utils import timezone
import random
import urllib2
import json


def get_challenge(status): 
     """
     Get today's challnege
     """
     status.success = False
     status.data["curr_challenge"] = {}
 
     # get current challenge object from database
     now = datetime.date.today()
#     now = now.replace(hour=0, minute=0, second=0, microsecond=0)
     m = models.Challenge.objects.filter(pub_date__gt=now)
     if len(m) == 1:
         # return challenge object and set success
         status.data["curr_challenge"] = m[0]
         status.success = True
     elif m:
         status.errors.append("Somehow there was more than one challenge today, in the future this should probably just use the first one")
     else:
         status.errors.append("There was no challenge today")
 
     return status
