def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        # _ ar en variabel, och en variabel ar vad som helst. Darfor analogt med else i nedre exemplet.
        case _:
            return "Something's wrong with the internet"

def http_error(status):
    if status == 400:
        return "Bad request"
    elif status == 404:
        return "Not found"
    elif status == 418:
        return "I'm a teapot"
    else:
        return "Something is wrong with the internet"