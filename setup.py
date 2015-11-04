from setuptools import setup

setup(
      name = 'keepalive',
      version = "0.2.dev0",
      description = 'urllib keepalive support for python3',
      long_description = 'An HTTP handler for `urllib2` that supports HTTP 1.1 and keepalive in Python 3.x.',
      license = 'GNU GPL',
      author = "Benjamin Woodruff",
      author_email = "github@benjam.info",
      maintainer = 'Sergio Fernandez',
      maintainer_email = 'sergio@wikier.org',
      url = 'https://github.com/wikier/keepalive',
      download_url = 'https://github.com/wikier/keepalive/releases',
      platforms = ['any'],
      packages = ['keepalive'],
      requires = [],
      install_requires = [],
      classifiers =  [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
      ],
      keywords = 'python http urllib keepalive'
)
