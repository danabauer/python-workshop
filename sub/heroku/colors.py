from itty import *
import redis


@get('/')
def do_it(_):
    """Show the web page."""

    return serve_static_file(_, 'colors.html', root)


@get('/color')
def do_it(_):
    """Get the color that is currently stored in the bucket."""

    bucket = get_a_bucket()

    color = bucket.get('color') or 'white'
    return color


@post('/color')
def do_it(request):

    color = request.body
    bucket = get_a_bucket()

    bucket.set('color', color)
    return color


def get_a_bucket():
    """Get the variable bucket ready."""

    bucket = redis.Redis(
        host='tetra.redistogo.com',
        password='a0577641ea43385552c5a1cdf120d437',
        port=9463,
        db=0)
    return bucket


import os
root = os.path.dirname(__file__)
port = int(os.environ.get('PORT', 8080))
run_itty(host='0.0.0.0', port=port)
