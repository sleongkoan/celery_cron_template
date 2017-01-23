import os

from setuptools import setup, find_packages

import __version__

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

requires = [
    'celery',
    'flower',
    'redis'
]

setup(
    name='glorified_cron',
    version=__version__.VERSION,
    description='Celery app used as glorified cron.',
    long_description=README,
    classifiers=[
        "Programming Language :: Python"
    ],
    author='Stephen Leong Koan',
    author_email='sleongkoan@gmail.com',
    url='',
    keywords='celery, periodic task, cron alternative',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    setup_requires=requires + ['pytest-runner']
)
