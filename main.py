from biblioteca.model.livro import Livro, LivroBuilder
from biblioteca.model import usuario

if __name__ == '__main__':
    teste = (LivroBuilder()
                .addAutor('dd')
                .addGenero('da')
                .addId(2)
                .addStatus()
                .addTitulo('hahaha')
                .addIsbn('324')
                .build())
    
    print(teste)