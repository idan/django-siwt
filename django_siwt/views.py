import oauth, httplib, time, datetime

try:
    import simplejson
except ImportError:
    try:
        import json as simplejson
    except ImportError:
        try:
            from django.utils import simplejson
        except:
            raise "Requires either simplejson, Python 2.6 or django.utils!"

from django.http import *
from django.shortcuts import render_to_response, redirect
from django.core.urlresolvers import reverse

from django_siwt.utils import *

CONSUMER = oauth.OAuthConsumer(SIWT_CONSUMER_KEY, SIWT_CONSUMER_SECRET)
CONNECTION = httplib.HTTPSConnection(SERVER)
SIGNIN_NEXT_DEFAULT_URL = getattr(settings, 'SIWT_SIGNIN_NEXT_DEFAULT_URL', '/')
SIGNOUT_NEXT_DEFAULT_URL = getattr(settings, 'SIWT_SIGNOUT_NEXT_DEFAULT_URL', '/')

def signin(request):
    "Start the SIWT flow."
    token = get_unauthorised_request_token(CONSUMER, CONNECTION)
    auth_url = get_authorisation_url(CONSUMER, token)
    request.session['unauthed_token'] = token.to_string()
    request.session['siwt_next'] = request.REQUEST.get('next', None)
    return redirect(auth_url)

def callback(request):
    "Handle browsers returning from SIWT."
    unauthed_token = request.session.get('unauthed_token', None)
    siwt_next = request.session.get('siwt_next', SIGNIN_NEXT_DEFAULT_URL)
    # TODO: handle failures more gracefully
    if not unauthed_token:
        return HttpResponse("No un-authed token cookie")
    token = oauth.OAuthToken.from_string(unauthed_token)   
    if token.key != request.GET.get('oauth_token', 'no-token'):
        return HttpResponse("Something went wrong! Tokens do not match")
    access_token = exchange_request_token_for_access_token(CONSUMER, CONNECTION, token)
    request.session['access_token'] = access_token.to_string()
    return redirect(siwt_next)

def signout(request):
    request.session.clear()
    next = request.REQUEST.get('next', None)
    if next:
        return redirect(next)
    else:
        return redirect(SIGNOUT_NEXT_DEFAULT_URL)