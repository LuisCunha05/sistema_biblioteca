from hashlib import sha256

def toHash(string: str) -> str:
    """Returns the Hash of the given string using SHA256"""
    return sha256(string.encode()).hexdigest()

def unpackValue(value: tuple[int|str|None]) -> int|str:
    """Retorna o valor da Tuple de um elemento or raise ValueError quando valor recebido é None"""
    if(value is None):
        raise ValueError('Valor não existe')
    return value[0]


if __name__ == '__main__':
    print(toHash('oi'))
    print(unpackValue((None,)))