from itty import *
import tropo
import redis


@get('/')
def webpage(_):

    print 'hello'
    return serve_static_file(_, 'colors.html', root)


@get('/color')
def color(_):

    store = get_redis_ready()
    color = store.get('color') or 'white'
    return color


@post('/change_color/(.*)')
def change_color(_, color):

    phone = get_tropo_ready()
    store = get_redis_ready()
    store.set('color', color)


def get_tropo_ready():
    """Get the phone service ready."""
    return tropo.Tropo


def get_redis_ready():
    """Get the variable bucket ready."""
    store = redis.Redis(
        host='tetra.redistogo.com',
        password='a0577641ea43385552c5a1cdf120d437',
        port=9463,
        db=0)
    return store


import os
root = os.path.dirname(__file__)
port = os.environ.get('PORT') or 8080
run_itty(port=port)
