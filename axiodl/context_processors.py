from django.conf import settings


def recaptcha_site_key(request):
    return {'GOOGLE_RECAPTCHA_SITE_KEY': settings.GOOGLE_RECAPTCHA_SITE_KEY}
