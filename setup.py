import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

README = read('README.md')

setup(
    name = "django_gmapsfield",
    version = "0.1",
    url = 'http://github.com/mintchaos/django_compressor',
    license = 'MIT and GPL',
    description = "Compresses linked and inline javascript or CSS into a single cached file.",
    long_description = README,

    author = 'Bocoup, LLC',
    author_email = 'tim@bocoup.com',
    packages = [
        'gmapsfield',
    ],
    package_data = {
        'gmapsfield': [
                'templates/gmapsfield/*.html',
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
