from django.conf import settings
from django.core.exceptions import MiddlewareNotUsed
from .utils.client import Client

class AirbrakeNotifierMiddleware(object):
    def __init__(self):
        self.client = Client()

    def process_exception(self, request, exception):
        if hasattr(settings, 'AIRBRAKE') and not settings.AIRBRAKE.get('DISABLE', False):
            try:
                self.client.notify(exception=exception, request=request)
            # Ignore failures from issues like rate limiting
            except:
                pass
