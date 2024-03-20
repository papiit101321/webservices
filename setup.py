from __future__ import with_statement
import os

from setuptools import setup, find_packages

from mezzanine_firestore import __version__ as version

install_requires = [
    "mezzanine >= 4.0", 
    #"django-type-of-works>=0.1",
    #"django-registration-redux>=1",
    #"django-countries>=3",
]

try:
    setup(
        name="plugin_firestore",
        version=version,
        author="Noemi Salazar",
        author_email="papiit101321@gmail.com",
        description="Connection to abejas firestore.",
        long_description=open("README.rst").read(),
        license="BSD",
        #url="http://mezzanine.jupo.org/",
        zip_safe=False,
        include_package_data=True,
        packages=find_packages(),
        install_requires=install_requires,
        entry_points="""
            [console_scripts]
        """,
        classifiers=[
            "Development Status :: 4 - Beta",
            "Environment :: Web Environment",
            "Framework :: Django",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: BSD License",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Topic :: Internet :: WWW/HTTP",
            "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
            "Topic :: Internet :: WWW/HTTP :: WSGI",
            "Topic :: Software Development :: Libraries :: "
                                                "Application Frameworks",
            "Topic :: Software Development :: Libraries :: Python Modules",
        ],)
except:
    pass
