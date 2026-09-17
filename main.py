def is_strong_password(password):
    """
    Checks if a password is strong based on the following criteria:
    - At least 8 characters long
    - Contains at least one number (digit)
    - Contains at least one uppercase letter

    Returns True if all conditions are met, False otherwise.
    """
    if len(password) < 8:
        return False

    has_number = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)

    return has_number and has_upper