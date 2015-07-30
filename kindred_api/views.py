from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from kindred_api import controller
from kindred_api.serializers import *

#objects

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class Status(object):
    def __init__(self, success=False, data={}, exceptions=[], errors=[], status_code=403):
        self.success = success
        self.data = data
        self.exceptions = exceptions
        self.errors = errors
        self.status_code = status_code

    def serialize(self):
        temp = {}
        temp["success"] = self.success
        temp["data"] = self.data
        temp["exceptions"] = self.exceptions
        temp["errors"] = self.errors
        return temp

#Get methods

@csrf_exempt
@api_view(['GET'])
def get_todays_challenge(request):
    """
    Get the current day's challenge 
    """
    
    retval = Status(success=False, data={}, exceptions=[], errors=[], status_code=403)
    try:
         if request.method == 'GET':
            #should probably do a pearing and authenticate here eventually
             retval = controller.get_challenge(retval)
             if retval.success:
                 retval.status_code = 200
                 retval.data["curr_challenge"] = (ChallengeSerializer(retval.data["curr_challenge"])).data
    except Exception as e:
        retval.exceptions.append(str(e))
        retval.success = False
        retval.status_code = 500

    return JSONResponse(retval.serialize(), status=retval.status_code)

@csrf_exempt
@api_view(['POST'])
def store_user(request):
    """
    Store a user
    """
    retval = Status(success=False, data={}, exceptions=[], errors=[], status_code=403)
    print request.DATA
    if "username" in request.DATA:
    	try:
            if request.method == 'POST':
            	user = UserSerializer(data=request.DATA)
                if user.is_valid():
                	user = user.create(user.validated_data)
                	print user
                	retval = controller.store_user(retval, user)
                	print retval.data
                	if retval.success:
                		retval.status_code = 200
                		retval.data["user"] = (UserSerializer(retval.data["user"])).data
                        print retval.data["user"]
        except Exception as e:
            retval.exceptions.append(str(e))
            retval.success = False
            retval.status_code = 500
            print retval.exceptions 

    return JSONResponse(retval.serialize(), status=retval.status_code)
        
@csrf_exempt
@api_view(['POST'])
def store_photo(request):
    """
    Store a photo 
    """
    
    retval = Status(success=False, data={}, exceptions=[], errors=[], status_code=403)
    print request.DATA
    print "we just printed data"
    #print uploaded_file.name
    if request.DATA["user"] and request.FILES["file"]:
        try:
            if request.method == 'POST':
                #authenticate here eventually
                photo = PhotoSerializer(data=request.DATA)
                #print photo
                photo_valid = photo.is_valid()
                print photo.errors
                if photo_valid:
                    photo = photo.create(photo.validated_data)
                    retval = controller.store_photo(retval, request.FILES["file"], photo)
                    if retval.success:
                        retval.status_code = 200
                        retval.data["photo"] = (ChallengeSerializer(retval.data["curr_challenge"])).data
         
        except Exception as e:
            retval.exceptions.append(str(e))
            retval.success = False
            retval.status_code = 500
            print retval.exceptions 

    return JSONResponse(retval.serialize(), status=retval.status_code
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            )
