import colorama


def debug(text: str):
    print(colorama.Fore.LIGHTCYAN_EX + text + colorama.Fore.RESET)


def debug_text(text: str):
    return colorama.Fore.LIGHTCYAN_EX + text + colorama.Fore.RESET
