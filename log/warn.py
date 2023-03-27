import colorama


def warn(text: str):
    print(colorama.Fore.LIGHTYELLOW_EX + text)


def warn_text(text: str):
    return colorama.Fore.LIGHTYELLOW_EX + text
