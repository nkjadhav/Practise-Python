try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description' : 'My Project',
    'Author'  : 'My Name',
    'url' : 'URL to get it',
    'download_url' : 'where to download it',
    'author_email' : 'My email',
    'version' : '0.1',
    'install_requires' : ['nose'],
    'packages' : ['NAME'],
    'scripts' : '[]',
    'name' : 'test'
}

setup(**config)
