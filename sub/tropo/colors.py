from httplib import HTTPConnection
# This script also uses two function from the Tropo module: 'ask', and 'say'.
# Normally this would look like:
#
# from tropo import ask, say
#
# However, in this case, these functions are imported automatically from the
# 'tropo' module on Tropo's server.


color_names = (
    'White, Black, Gray, Red, Maroon, Orange, Brown, Yellow, Olive, '
    'Lime, Green, Cyan, Teal, Blue, DarkBlue, Fuchsia, Violet, Purple')


def run():

    say("Tell me a color and I'll show it to you.")

    while True:

        answer = ask("What color do you want?",
                     {'choices': color_names + ', Stop'})

        if answer.value == 'NO_MATCH':
            say("I'm sorry, I didn't understand.  Please try again.")

        elif answer.value == 'Stop':
            say("Ok, I'll stop.  Goodbye.")
            break

        else:
            color = answer.value
            save(color)
            say("Ok, I'll change the color to " + color)


def save(color):
    conn = HTTPConnection('tropo-colors.herokuapp.com')
    conn.request('POST', '/color', body=color)


run()
