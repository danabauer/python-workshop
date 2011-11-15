import os
import urlparse

ROOT = os.path.dirname(__file__)

##
# Redis

redis_info = urlparse.urlparse(os.environ.get('REDISTOGO_URL', 'redis://user:pass@host:9999/'))

REDIS = {
    'host':     redis_info.hostname,
    'password': redis_info.password,
    'port':     redis_info.port,
    'db':       0,
}

##
# The itty web framework

ITTY = {
    'host': '0.0.0.0',
    'port': int(os.environ.get('PORT', 8080))
}
