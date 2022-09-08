from django.shortcuts import render, redirect
from . import service
from django.contrib import messages
from django.urls import reverse


# Create your views here.
def shorten(request,
            url,
            expiredDate):
    shortened_url_hash = service.shorten(url, expiredDate)
    shortened_url = request.build_absolute_uri(reverse('redirect', args=[shortened_url_hash]))
    if expiredDate:
        messages.info(request, f"The link will be expire at {expiredDate}.")
    else:
        messages.info(request, f"The link will be expired after 15 minutes.")
    return render(request, 'main/link.html', {'shortened_url': shortened_url})


def index(request):
    return render(request, 'main/index.html')


def shorten_post(request):
    return shorten(request, request.POST['url'], request.POST.get('expiredDate', 0))


def redirect_hash(request,
                  url_hash):
    original_url = service.load_url(url_hash)
    if original_url:
        return redirect(original_url)
    else:
        shortened_url = request.build_absolute_uri(reverse('redirect', args=[url_hash]))
        return render(request, 'main/link.html', {'shortened_url': shortened_url, 'message': 2})


def custom_url(request):
    previousURL = request.POST['shortenURL']
    customURL = request.POST['customURL']
    custom_hash = service.customUrl(previousURL,
                                    customURL)
    if custom_hash:
        shortened_url = request.build_absolute_uri(reverse('redirect', args=[custom_hash]))
        return render(request, 'main/link.html', {'shortened_url': shortened_url})
    else:
        return render(request, 'main/link.html', {'shortened_url': previousURL, 'message': 1})
