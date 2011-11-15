def run():

    say("Tell me a color and I'll show it to you.")

    while True:

        answer = ask("What color do you want?",
                     {'choices': color_names})

        if answer.value == 'NO_MATCH':
            say("I'm sorry, I didn't understand.  Please try again.")

        elif answer.value == 'Stop':
            say("Ok, I'll stop.  Goodbye.")
            break

        else:
            color = answer.value
            save(color)
            say("Ok, I'll change the color to " + color)
