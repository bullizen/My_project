def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 4
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

# ex, ask_ok alla parametrar angavs
print("svar", ask_ok("Food? ", 999, "Remind"))

# ex, ask_ok prompt och retries angavs
print("svar", ask_ok("Food? ", 999))

# ex, ask_ok prompt angavs
print("svar", ask_ok("Food? "))