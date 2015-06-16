from setuptools import setup, find_packages
import os
import platform

DESCRIPTION = "A simple python module to extract contact info from HTML pages"

LONG_DESCRIPTION = None
try:
    LONG_DESCRIPTION = open('README.md').read()
except:
    pass

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

setup(
    name='htmlcontact',
    version='0.1',
    author=u'tristan tao',
    author_email='tristan@teamleada.com',
    py_modules=['htmlcontact'],
    url='http://github.com/tristantao/html-contact',
    license='MIT',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    platforms=['any'],
    classifiers=CLASSIFIERS,
    install_requires=['beautifulsoup4', 'nltk'],
)
