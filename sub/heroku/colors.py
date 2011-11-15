from css_color_names import color_names
from itty import *
import tropo
import redis


@get('/')
def _(request):
    return serve_static_file(request, 'colors.html', root)


@get('/color')
def _(request):
    bucket = get_a_bucket()

    color = bucket.get('color') or 'white'
    return color


@post('/ask-for-color')
def _(request):
    phone = get_a_phone()

    ask_for_a_new_color(phone)
    return phone.RenderJson()


@post('/change-color')
def _(request):
    bucket = get_a_bucket()
    phone = get_a_phone()

    result = tropo.Result(request.body)
    color = result.getValue()

    agree_to_change_the_stored_color(phone, color)
    change_the_stored_color(bucket, color)
    ask_for_a_new_color(phone)
    return phone.RenderJson()


@post('/dont-understand')
def _(request):
    phone = get_a_phone()

    say_i_dont_understand(phone)
    ask_for_a_new_color(phone)
    return phone.RenderJson()


def agree_to_change_the_stored_color(phone, color):
    phone.say("Ok, I'll change the page color to " + color)


def change_the_stored_color(bucket, color):
    bucket.set('color', color)


def ask_for_a_new_color(phone):
    phone.ask(say='Pick a color.',
              choices=color_names)
    phone.on(event='continue', next='/change-color')
    phone.on(event='incomplete', next='/dont-understand')


def say_i_dont_understand(phone):
    phone.say("I'm sorry, I didn't understand that color.")


def get_a_phone():
    return tropo.Tropo()


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
