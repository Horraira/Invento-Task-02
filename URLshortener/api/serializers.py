from rest_framework import serializers
from main.models import LinkMapping
from main.service import *
import random
import string
from django.utils import timezone


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkMapping
        fields = '__all__'


class UrlShortenCreator(serializers.ModelSerializer):
    class Meta:
        model = LinkMapping
        fields = '__all__'


class UrlShorten(serializers.ModelSerializer):
    class Meta:
        model = LinkMapping
        fields = ['original_url', 'deletion_date']

    def create(self, validated_data):
        originalUrl = validated_data.pop("original_url")
        try:
            expiredDate = validated_data.pop("deletion_date")
        except KeyError:
            expiredDate = ''

        random_hash = ''.join(
            random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(7))
        if expiredDate:
            expired_date = expiredDate
        else:
            expired_date = timezone.now() + timezone.timedelta(minutes=15)

        url, created = LinkMapping.objects.update_or_create(
            original_url=originalUrl,
            hash=random_hash,
            creation_date=timezone.now(),
            deletion_date=expired_date,
        )
        return url
