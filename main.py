from biblioteca.model.livro import Livro, LivroBuilder
from biblioteca.model import usuario
from biblioteca.controller.controller_usuario import ControllerUsuario

if __name__ == '__main__':
    #teste = ControllerUsuario.instanceFromDB('555.666.777-88')
    #print(teste)

    def teste(a = None, b = None, c = None, d = None):
        arr = []

        map(lambda x: arr.append if x is not None else print('nah'), [a,b,c,d])

        print(arr)

    teste(b=3, d='oi')