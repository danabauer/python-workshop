from httplib import HTTPConnection


color_names = (
    'White, Black, Gray, Red, Maroon, Orange, Brown, Yellow, Olive, '
    'Lime, Green, Cyan, Teal, Blue, DarkBlue, Fuchsia, Violet, Purple')


def run():

    # The statement "while True" is the same as "forever".
    while True:

        # One "=" tells Python to store the value in the variable.
        answer = ask("What color do you want?", {'choices': color_names})
        color = answer.value

        # Two "==" means "is equal to".
        if color == 'NO_MATCH':
            say ("I'm sorry, I didn't understand.  Please try again.")

        else:
            save_color(color)
            say("Ok, I'll change the color to " + color)


def save_color(color):
    conn = HTTPConnection('tropo-colors.herokuapp.com')
    conn.request('POST', '/color', body=color)


run()
