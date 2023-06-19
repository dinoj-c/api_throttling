from django.http import HttpResponseForbidden
from django.utils import timezone
from django.conf import settings as SETTINGS

from datetime import timedelta

from .models import Throttle


class ThrottlingMiddleware:
    def __init__(self, get_response, requests_per_second=SETTINGS.THROTTLING_REQUEST_LIMIT):
        self.get_response = get_response
        self.requests_per_second = requests_per_second

    def __call__(self, request):
        referrer = request.META.get('HTTP_REFERER')

        if referrer:
            current_time = timezone.now()
            time_window_start = current_time - timedelta(seconds=1)
            recent_requests = Throttle.objects.filter(referrer=referrer, request_time__gte=time_window_start)
            if recent_requests.count() >= self.requests_per_second:
                return HttpResponseForbidden('Request limit exceeded')

            Throttle.objects.create(referrer=referrer, request_time=current_time)

        response = self.get_response(request)

        return response


