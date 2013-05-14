import os
import urlparse

ROOT = os.path.dirname(__file__)

##
# Redis -- a data store
#
# Redis is the data storage system that we use for this project.  It allows you
# to store data in really simple ways.  Heroku gives us easy access to a redis
# data store using a service called Redis To Go.  We have to parse out the
# pieces to use it.

redis_info = urlparse.urlparse(os.environ.get('REDISTOGO_URL', 'redis://user:pass@host:9999/'))

REDIS = {
    'host':     redis_info.hostname,
    'password': redis_info.password,
    'port':     redis_info.port,
    'db':       0,
}

##
# itty -- a web framework
#
# There are several web frameworks for Python, and each give you different
# built-in capabilities.  For this application, we want to use as simple a
# framework as possible, and itty is about as simple as it gets.  Here we set
# up the "host" and "port" (two things that are fundamental to being able to
# locate things on the web) that Heroku expects to use.

ITTY = {
    'host': '0.0.0.0',
    'port': int(os.environ.get('PORT', 8080))
}
