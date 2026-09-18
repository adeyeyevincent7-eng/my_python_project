def format_name(raw_name):
    try:
        #1. Look inside the name. if it contains a number, cause an error on purpose!
        if any(char.isdigit() for char in raw_name):
            raise ValueError("Names cannot have number!")
        #2. Trim extra spaces (.strip) and fix capitals (.title)
        return raw_name.strip().title()
    except Exception:
        # If anything goes wrong (empty text, numbers, wrong types), return this fallback
        return "Invalid Name"
print(format_name("SHOla1"))