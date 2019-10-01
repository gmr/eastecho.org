"""
Download and cache Instagram photos from a feed

"""
import io
import logging

from django_instagram import scraper
from django.conf import settings
from django.core.files import storage
import requests

LOGGER = logging.getLogger(__name__)


def get_photos(username):
    photos = []
    fs = storage.FileSystemStorage(location=settings.MEDIA_ROOT)
    for short_code, url in _get_photo_list(username):
        if not fs.exists(short_code):
            response = requests.get(url)
            if not response.ok:
                LOGGER.error('Error fetching image: %r', response.status_code)
                continue
            fs.save(short_code, io.BytesIO(response.content))
        photos.append(fs.url(short_code))
    return photos


def _get_photo_list(username):
    profile = scraper.instagram_profile_obj(username)
    user = profile['entry_data']['ProfilePage'][0]['graphql']['user']
    return [(e['node']['shortcode'],
             'https://www.instagram.com/p/{}/media/'.format(
                 e['node']['shortcode']))
            for e in user['edge_owner_to_timeline_media']['edges']]


def get_ig_url(short_code: str) -> str:
    url = 'https://www.instagram.com/p/{}/media/'.format(short_code)
    response = requests.get(url, allow_redirects=False)
    if response.status_code != 302:
        raise RuntimeError('Unexpected response')
    return response.headers['Location']
