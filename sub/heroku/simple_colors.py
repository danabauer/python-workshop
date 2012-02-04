from itty import *
import redis
import settings


##
#   Path : /
# Method : GET
#
# This is the main path for the application.  It just gives you the html page
# that you use to view the app.  For example, in your browser, go to the url:
#
#    http://tropo-colors.herokuapp.com/
#
# (The last '/' on that url because of the definiton below)
#
@get('/')
def _(request):
    return serve_static_file(request, 'colors.html', settings.ROOT)


##
#   Path : /color
# Method : GET
#
# This is the path that will allow you to get the current color from the
# database.  For example, in your browser, go to:
#
#    http://tropo-colors.herokuapp.com/color
#
# We use this to tell the web page what color it should be.
#
@get('/color')
def _(request):
    bucket = get_a_bucket()

    color = bucket.get('color') or 'white'
    return color


##
#   Path : /color
# Method : POST
#
# This path can also be used to set the current color for the web page.  Notice
# that this definition starts with @post instead of @get like the others.  By
# convention, on the web, GET usually means "retrieve something", and POST means
# "store something".  So, in this case, we're storing the color.
#
@post('/color')
def _(request):
    bucket = get_a_bucket()

    color = request.body
    bucket.set('color', color)
    return color


##
# This function will return a bucket (a Redis data storage structure) that we
# can use to store or retrieve colors.
def get_a_bucket():
    bucket = redis.Redis(**settings.REDIS)
    return bucket


run_itty(**settings.ITTY)
