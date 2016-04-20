from django.conf import settings
from django.http import HttpResponse
import simplejson


def index(request):
    return HttpResponse("Hey this is the home page!")