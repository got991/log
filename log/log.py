import colorama


def log(text):
    print(colorama.Fore.RESET + text)
def log_text(text):
    return colorama.Fore.RESET + text


