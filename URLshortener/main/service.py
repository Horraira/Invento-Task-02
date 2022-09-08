import random
import string
from django.utils import timezone
from django.urls import reverse
from .models import LinkMapping


def shorten(url, expiredDate):
    random_hash = ''.join(
        random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(7))
    if expiredDate:
        expired_date = expiredDate
    else:
        expired_date = timezone.now() + timezone.timedelta(minutes=15)
    mapping = LinkMapping(original_url=url, hash=random_hash, creation_date=timezone.now(), deletion_date=expired_date)
    mapping.save()
    return random_hash


def customUrl(shortenURL,
              customURL):
    allHash = LinkMapping.objects.all()
    for foo in allHash:
        if foo.hash == customURL:
            return 0

    oldHash = shortenURL.split('/')[-1]
    url = LinkMapping.objects.get(hash=oldHash).original_url

    expired_date = timezone.now() + timezone.timedelta(minutes=15)
    mapping = LinkMapping(original_url=url, hash=customURL, creation_date=timezone.now(), deletion_date=expired_date)
    mapping.save()
    return customURL


def load_url(url_hash):
    try:
        original_url = LinkMapping.objects.get(hash=url_hash, deletion_date__gt=timezone.now()).original_url
        return original_url
    except LinkMapping.DoesNotExist:
        return 0
