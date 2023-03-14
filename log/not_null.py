
from .debug import debug_text
def not_null_str(string):
    if not string == "":
        print(debug_text("Checked: String Not Equal \"\""))
        return True
    elif not string == " "
        print(debug_text("Checked: String Not Equal \" \""))
        return True
    else:
        return False