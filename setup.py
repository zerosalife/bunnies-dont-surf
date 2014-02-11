try:
    from setuptools import setup
except ImportError:
    print "setuptools is not installed"
    from distutils.core import setup

config = {
    "description" : "My Project",
    "author" : "Cliff Rodgers",
    "url" : "URL to get it at.",
    "download_url" : "where to download it",
    "author_email" : "frodgers@wisc.edu",
    "version" : "0.1",
    "install_requires" : ["nose"],
    "scripts" : [],
    "name" : "projectname"
}

setup(**config)
