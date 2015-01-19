from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from app.models import ApplicationState, ShortenedURL
from base64 import b64encode

@csrf_exempt
def shorten(request):
    # if request.method == "POST":
    if True:
        url = request.GET["url"]
        appstate = ApplicationState.objects.first()        
        next_id = appstate.next_id
        short_id = b64encode(str(next_id))
        shortened_url = ShortenedURL.objects.create(original_url=url, shrtd = short_id)
        appstate.next_id += 1
        appstate.save()
        return HttpResponse("original: {0} shortened: {1}".format(url, short_id))
        
    
