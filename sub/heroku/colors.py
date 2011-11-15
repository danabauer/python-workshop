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


def get_a_bucket():
    """Get the variable bucket ready."""

    bucket = redis.Redis(
        host='tetra.redistogo.com',
        password='a0577641ea43385552c5a1cdf120d437',
        port=9463,
        db=0)
    return bucket


##
# This is for the simple Tropo script version of the program.  Upload the script
# in tropo/colors.py to your Tropo account, and point the URL in that file to
# the following route.

@post('/color')
def do_it(_):

    color = _.body
    bucket = get_a_bucket()

    bucket.set('color', color)
    return color


##
# This is for a more complex version of the program.  It does not rely on any
# Tropo-hosted scripts.  Point a Tropo app at the following route to start the
# program.

from css_color_names import color_names
import tropo

@post('/ask-for-color')
def do_it(_):

    phone = get_a_phone()

    ask_for_a_new_color(phone)
    return phone.RenderJson()


@post('/change-color')
def do_it(_):

    result = tropo.Result(_.body)
    color = result.getValue()

    bucket = get_a_bucket()
    phone = get_a_phone()

    agree_to_change_the_stored_color(phone, color)
    change_the_stored_color(bucket, color)
    ask_for_a_new_color(phone)

    return phone.RenderJson()


@post('/dont-understand')
def do_it(_):

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
    """Get the phone service ready."""

    return tropo.Tropo()


import os
root = os.path.dirname(__file__)
port = int(os.environ.get('PORT', 8080))
run_itty(host='0.0.0.0', port=port)
