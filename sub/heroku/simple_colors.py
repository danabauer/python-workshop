from itty import *
import redis
import settings


@get('/')
def _(request):
    return serve_static_file(request, 'colors.html', settings.ROOT)


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
    bucket = redis.Redis(**settings.REDIS)
    return bucket


run_itty(**settings.ITTY)
