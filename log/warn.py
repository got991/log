import colorama


def warn(text):
    print(colorama.Fore.LIGHTYELLOW_EX + text)


def warn_text(text):
    return colorama.Fore.LIGHTYELLOW_EX + text
