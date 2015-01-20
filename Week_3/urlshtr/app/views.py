from base64 import b64encode

from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from app.models import ShortenedURL


def home(request):
    return render(request, 'home.html')    
 


def shorten(request):
    if request.method == "POST":
        url = request.POST["url"]
        pre_existing_shortenings = ShortenedURL.objects.filter(original_url=url)
        if pre_existing_shortenings:
            short_id = pre_existing_shortenings[0].shrtd
        else:            
            shortened_url = ShortenedURL.objects.create(original_url=url)
            short_id = b64encode(str(shortened_url.id))
            shortened_url.shrtd = short_id
            shortened_url.save()        
        return render(request, 'result.html', {"original": url, "shortened": short_id})
    else:
        return redirect('home')
        
    
    
def elsewhere(request, shortened_url):    
    in_database = ShortenedURL.objects.filter(shrtd=shortened_url)
    if in_database:
        return redirect(in_database[0].original_url)
    else:
        raise Http404
        

    
