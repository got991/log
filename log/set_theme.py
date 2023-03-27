import colorama


def show_theme(theme):
    """

    :type theme: str | bytes | int
    """
    num_theme = int(theme)
    theme_is_true = num_theme == 1 or num_theme == 2 or num_theme == 3
    if theme_is_true:
        match num_theme:
            case 1:
                print(colorama.Fore.RESET)
                # [2023/03/27 12:29:01] [Thread01:infoType]: Your Message...
