import secrets


def randint(a, b):
    return secrets.choice(range(a, b+1))
