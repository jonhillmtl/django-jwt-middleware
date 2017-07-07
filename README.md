## Django JSON Web Token Middleware

### Motivation

This middleware should gel well with a JSON Web Token based microservice architecture.

On every request, the middleware will check for a `jwtoken` in the `GET` or `POST` data,
and decrypt it. It shows up as `request.user`... beware, it's not a real Django user, but
a dictionary describing one provided by the authentication/login service. An AnonymousUser object
is loaded if no `jwtoken` can be found or decrypted.

### Installing

- `pip install git+https://github.com/jonhillmtl/django-jwt-middleware`

Adjust your settings file:

```
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django_jwt_middleware.DjangoJSONWebTokenMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

Remove the authentication middleware completely, if you want. I haven't tested it with it in the Middleware, though.

Finally, export a `JWT_KEY` into the environment.

`export JWT_KEY=<a key>`
    
For this to work at all, it has to be the same key, and algorithms, as a key from the login micro-service.

Best practices on how to share that key betweens services to follow.

### Example project

`example` contains an example Django project implementing the service.

I used Postman during development to hit the `test_middleware/` url, with PUT, POST, DELETE, and GET calls. `jwtoken` was, naturally, set. Try it out.

### TODO

- support other encryption algorithms
- read the JWT_KEY from kerberos
