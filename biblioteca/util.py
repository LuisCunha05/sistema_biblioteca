from hashlib import sha256
import os, sys

def toHash(string: str) -> str:
    """Returns the Hash of the given string using SHA256"""
    return sha256(string.encode()).hexdigest()

def unpackValue(value: tuple[int|str|None]) -> int|str:
    """Retorna o valor da Tuple de um elemento or raise ValueError quando valor recebido é None"""
    if(value is None):
        raise ValueError('Valor não existe')
    return value[0]

def basePath(file:str = None) -> str:
    """
    Retorna o caminho para a pasta atual em que o script se encontra. Util para adicionar caminho para imagens e outros.

    Args:
        file: Um arquivo ou pasta específica, podendo conter outro caminho.

    Returns:
        Uma string contendo o caminho como: 'C:\\users\\joaozinho\\py'.

    Examples:
        basePath()\n
        ->\t'C:\\users\\joaozinho\\py'\n
        basePath('imagem.png')\n
        ->\t'C:\\users\\joaozinho\\py\\imagem.png'
    """
    if(file):
        return os.path.dirname(os.path.abspath(sys.argv[0])) + f'\\{file}'
    return os.path.dirname(os.path.abspath(sys.argv[0]))

if __name__ == '__main__':
    # print(toHash('oi'))
    # print(unpackValue((None,)))
    print(basePath())