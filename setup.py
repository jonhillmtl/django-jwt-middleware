from distutils.core import setup

setup(name='django-jwt-middleware',
      version='0.1',
      description='Django JSON Web Token middleware',
      author='Jon Hill',
      author_email='jon@jonhill.ca',
      url='https://github.com/jonhillmtl/django-jwt-middleware',
      license='MIT',
      packages = ['django_jwt_middleware'],
      install_requires=[
          "jwcrypto",
          "django"
      ],
)
