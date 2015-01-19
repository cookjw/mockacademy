from base64 import b64encode

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from app.models import ShortenedURL


@csrf_exempt
def shorten(request):
    # if request.method == "POST":
    if True:
        url = request.GET["url"]
        pre_existing_shortenings = ShortenedURL.objects.filter(original_url=url)
        if pre_existing_shortenings:
            short_id = pre_existing_shortenings[0].shrtd
        else:            
            shortened_url = ShortenedURL.objects.create(original_url=url)
            short_id = b64encode(str(shortened_url.id))
            shortened_url.shrtd = short_id
            shortened_url.save()
        return HttpResponse(
            "original: {0} shortened: {1}".format(url, short_id)
            )
        
    
