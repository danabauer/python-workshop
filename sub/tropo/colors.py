from httplib import HTTPConnection


color_names = (
    'White, Black, Gray, Red, Maroon, Orange, Brown, Yellow, Olive, '
    'Lime, Green, Cyan, Teal, Blue, DarkBlue, Fuchsia, Violet, Purple')


def run():

    say("Tell me a color and I'll show it to you.")

    while True:

        answer = ask("What color do you want?", {'choices': color_names})

        if answer.value == 'NO_MATCH':
            say ("I'm sorry, I didn't understand.  Please try again.")

        elif answer.value == 'Stop':
            say("Ok, I'll stop.  Goodbye.")
            break

        else:
            color = answer.value
            save_color(color)
            say("Ok, I'll change the color to " + color)


def save_color(color):
    conn = HTTPConnection('tropo-colors.herokuapp.com')
    conn.request('POST', '/color', body=color)


run()
