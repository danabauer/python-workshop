Tropo Colors
============

This is a simple application built with Redis and Tropo to change the color of
the background of a web page on voice command.  It is meant to be as simple as
possible, so that it can be used as an example to teach programming.

Explanation
-----------

There are three parts to this application:

  * A Tropo script (``tropo/colors.py``) that asks the user for a color,
  * A server-side Itty app (``heroku/simple_colors.py``) that handles the
    storage and retrieval of the current color from a Redis data store, and
  * A client-side script that checks on updates to the stored color.

The Tropo script is made to be uploaded to a Tropo account.  The Itty app can
be uploaded to Heroku (or anywhere else that can run and serve Python apps).

The Tropo app that you create to run the script should be assigned a phone
number.  When you call that number, Tropo will run the script, asking for a
color.  If it recognizes the color, it will send out a signal (``request``) to
the Itty app to save the color.  The Itty app will receive the ``request`` and
store the color in a Redis datastore (``bucket``).

In the mean time, the client side script will be watching the value of the
color stored in the ``bucket`` and, when it changes, updating the web page.

Why Itty?
---------

I normally create my apps in Django.  I could have created a Django project for
this, and used an SQLite database or something, but I wanted something that I
could do in about one module, and that I didn't have to do too much additional
explanation to get through.

So, I started to try Flask (zachwill has a great flask-heroku starter project
on github), but I found that even this seemed to obfuscate what I was trying
to get across.  In addition to my framework being light-weight, I wanted my
code to be as light-weight as possible as well, since this is a pedagogical
tool.  I don't mind Flask myself (as an experienced developer), but I felt that
things like::

    @request('/colors', methods=['POST'])
    ...

were too much.  Itty is the lightest, lowest-configuration framework for Python
I've seen, and gets the point across nicely.  For example, the above route in
Itty is::

    @post('/colors')
    ...

A minor difference to be sure, but one big enough to sway me.

Why two apps?
-------------

There are two Itty apps in the heroku folder.  At first, I used the Tropo web
API, but decided to simplify things by using a Tropo script instead for two
reasons:

  * I was afraid that the overhead of explaining the HTTP back-and-forth that
    is done between Tropo and the server app would get in the way of the
    programming concepts.
  * Using the script, I get to use more of simpler concepts like iteration and
    conditionals.
