common_passwords = [
    "password",
    "123456",
    "123456789",
    "admin",
    "qwerty",
    "welcome",
    "abc123",
    "letmein"
]

def dictionary_check(password):
    if password.lower() in common_passwords:
        return "Found in common password dictionary!"
    return "Not found in dictionary"