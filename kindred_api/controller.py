import datetime 
from kindred_api import models
from kindred_api.serializers import *
# TODO: why are serializers in here?
from django.utils import timezone
import random
import urllib2
import json
import os.path

def get_challenge(status): 
     """
     Get today's challnege
     """
     status.success = False
     status.data["curr_challenge"] = {}
 
     # get current challenge object from database
     now = datetime.date.today()
#     now = now.replace(hour=0, minute=0, second=0, microsecond=0)
     m = models.Challenge.objects.filter(pub_date=now)
     if len(m) == 1:
         # return challenge object and set success
         status.data["curr_challenge"] = m[0]
         status.success = True
     elif m:
         status.errors.append("Somehow there was more than one challenge today, in the future this should probably just use the first one")
#           status.data["curr_challenge"] = m[0]
#           status.success = True
     else:
         status.errors.append("There was no challenge today")
 
     return status

def store_user(status, user):
    """
    Store a user
    """
    status.success = False
    status.data["user"] = {}
    #this could be an interesting problem in the future, because you can change your instagram username?
    m = models.User.objects.filter(username=user.username)
    if len(m) >= 1:
    	status.errors.append("This user exists, somethings wrong.")
    else:
        m = user
        status.data["user"] = m 
        status.success = True 
        m.save() 

    return status 

def store_photo(status, up_file, file_data):
    """
    Store the file and the associated data
    """
    #update path to save files to www.getkindred.com/media/file_name.jpg
    dest_dir = "/Users/Toohey/django_projects/kindred/media/"

    #get the user, this seems really inefficient, to get the user every time for the infos we want
    user = models.User.objects.filter(pk = file_data.user.pk)
    #file name is date published + ig user number
    #user[0].username is a big assumption :p
    new_name = user[0].username + "_" + str(file_data.pub_date.year) + "-" + str(file_data.pub_date.month) + "-" + str(file_data.pub_date.day) + ".jpg"
    #make sure there are no spaces
    new_name = new_name.replace(" ", "_")
    #make the dir if it doesn't exist 
    try:
        os.mkdir(os.path( dest_dir ))
    except:
        pass

    full_filename = os.path.join( dest_dir + new_name )
    #if the file exists, something is poopy
    m = models.Photo.objects.filter(url=full_filename)
    if m:
        status.errors.append("This photo exists somehow, shit snacks")
        status.success = False
    else:
       
        #write the file out
        fout = open(full_filename, 'wb+')
        for chunk in up_file.chunks():
            fout.write(chunk)
        fout.close()
    
        file_data.url = full_filename
        status.success = True
        status.data["photo"] = file_data
        file_data.save() #breaks here

        
    return status
    
    

        


















