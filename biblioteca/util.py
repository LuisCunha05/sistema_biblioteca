from hashlib import sha256

def toHash(string: str) -> str:
    """Returns the Hash of the given string using SHA256"""
    return sha256(string.encode()).hexdigest()


if __name__ == '__main__':
    print(toHash('oi'))