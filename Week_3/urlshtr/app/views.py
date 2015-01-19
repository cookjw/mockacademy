from base64 import b64encode

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from app.models import ApplicationState, ShortenedURL


@csrf_exempt
def shorten(request):
    # if request.method == "POST":
    if True:
        url = request.GET["url"]
        shortened_url = ShortenedURL.objects.create(original_url=url)
        short_id = b64encode(str(shortened_url.id))
        shortened_url.shrtd = short_id
        shortened_url.save()
        return HttpResponse(
            "original: {0} shortened: {1}".format(url, short_id)
            )
        
    
