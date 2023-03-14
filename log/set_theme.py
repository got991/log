import colorama

from .not_null import not_null_str
def show_theme(theme):
    themeIsTrue = int(theme) == 1 or int(theme) == 2 or int(theme) == 3
    if not_null_str(theme) and themeIsTrue :
        pass
        # Todo: 展示theme