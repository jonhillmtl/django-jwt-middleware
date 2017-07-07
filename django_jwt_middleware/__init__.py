import os
import json

from django.contrib.auth.models import AnonymousUser
from django.conf import settings
from jwcrypto import jwt, jwk, jwe


def jwt_to_user_dictionary(jwtoken, jwt_key):
    try:
        key = jwk.JWK(**jwt_key)
        etoken = jwt.JWT(key=key, jwt=jwtoken)
        stoken = jwt.JWT(key=key, jwt=etoken.claims)
        return json.loads(stoken.claims)
    except jwe.InvalidJWEData:
        return {}


class DjangoJSONWebTokenMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.process_request(request)
        response = self.get_response(request)
        return response
        
    def process_request(self, request):
        from text_header import text_header
        request.user = AnonymousUser()
        
        jwtoken = None
        if request.method in ['GET', 'PUT', 'DELETE']:
            jwtoken = request.GET.get('jwtoken', None)
        elif request.method == 'POST':
            jwtoken = request.POST.get('jwtoken', None)
            
        if jwtoken is not None:
            request.user = jwt_to_user_dictionary(jwtoken, settings.JWT_KEY)
            
