from itty import *
import tropo
import redis


@get('/')
def webpage(_):

    return serve_static_file(_, 'colors.html', root)


@get('/color')
def color(_):

    store = get_redis_ready()
    color = store.get('color') or 'white'
    return color


@post('/ask-for-color')
def ask_for_a_new_color(_):

    phone = get_tropo_ready()
    phone.ask('Give me a color.')
    phone.on(event='continue', next='/change-color')
    return phone.RenderJson()


@post('/change-color')
def change_color(_):

    store = get_redis_ready()
    result = tropo.Result(_.body)
    color = result.getValue()
    store.set('color', color)
    return ask_for_a_new_color(_)


def get_tropo_ready():
    """Get the phone service ready."""

    return tropo.Tropo()


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
port = int(os.environ.get('PORT', 8080))
run_itty(host='0.0.0.0', port=port)
