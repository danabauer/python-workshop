color_names = (
    'White, Black, Gray, Red, Maroon, Orange, Brown, Yellow, Olive, '
    'Lime, Green, Cyan, Teal, Blue, DarkBlue, Fuchsia, Violet, Purple')


def save_color(color):
    from httplib import HTTPConnection
    conn = HTTPConnection('tropo-colors.herokuapp.com')
    conn.request('POST', '/change-color/' + color)


while True:
    answer = ask("What color do you want?", {'choices': color_names})
    color = answer.value

    if color == 'NO_MATCH':
        say ("I'm sorry, I didn't understand.  Please try again.")

    else:
        save_color(color)
        say("Ok, I'll change the color to " + color)
