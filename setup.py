import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

README = read('README.md')

setup(
    name = "django_gmapsfield",
    version = "alpha",
    url = 'http://github.com/bocoup/django_gmapsfield',
    license = 'MIT and GPL',
    description = "Django Google Maps Field is a robust way to customize and display a Google Map in Django, and use it as a UI for selecting/displaying location information in the Django admin.",
    long_description = README,

    author = 'Bocoup, LLC',
    author_email = 'tim@bocoup.com',
    packages = [
        'gmapsfield',
    ],
    package_data = {
        'gmapsfield': [
                'templates/*.html',
                'templates/admin/*.js',
            ],
    },
    requires = [
        'json',
        'Django',
    ],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
