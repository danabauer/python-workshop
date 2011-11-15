from itty import *
import redis


@get('/')
def _(request):
    return serve_static_file(_, 'colors.html', root)


@get('/color')
def _(request):
    bucket = get_a_bucket()

    color = bucket.get('color') or 'white'
    return color


@post('/color')
def _(request):
    bucket = get_a_bucket()

    color = request.body
    bucket.set('color', color)
    return color


def get_a_bucket():
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
