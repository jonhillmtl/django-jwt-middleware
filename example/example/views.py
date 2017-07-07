from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, AnonymousUser

@csrf_exempt
def test_middleware(request):
    if isinstance(request.user, AnonymousUser):
        return JsonResponse(dict(message="AnonymousUser", success=False))
    else:
        return JsonResponse(dict(user=request.user, success=True))