import colorama


def log(text: str):
    print(colorama.Fore.RESET + text)


def log_text(text: str):
    return colorama.Fore.RESET + text
