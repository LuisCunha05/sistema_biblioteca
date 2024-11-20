-- Active: 1730375618989@@10.28.2.34@3306@biblioteca

use biblioteca;

create table usuario (
    id_usuario int PRIMARY key AUTO_INCREMENT,
    nome VARCHAR(50),
    cpf VARCHAR(30) UNIQUE,
    senha VARCHAR(70),
    email VARCHAR(50) UNIQUE
);

create table livro (
    id_livro int primary key AUTO_INCREMENT,
    titulo VARCHAR(50),
    autor VARCHAR(50),
    genero VARCHAR(50),
    status_livro TINYINT, -- 1:disponivel,2-emprestado,3-extraviado,4-danificado
    isbn VARCHAR(50) UNIQUE
);

CREATE Table emprestimo (
    id_emprestimo int PRIMARY KEY AUTO_INCREMENT,
    id_livro int,
    id_usuario int,
    devolvido BOOLEAN,
    Foreign Key (id_livro) REFERENCES livro(id_livro),
    Foreign Key (id_usuario) REFERENCES usuario(id_usuario)
);

CREATE Table administrador (
    id_administrador int PRIMARY KEY AUTO_INCREMENT,
    id_usuario int,
    Foreign Key (id_usuario) REFERENCES usuario(id_usuario)
);

INSERT INTO livro (titulo, autor, genero, status_livro, isbn) VALUES
('O Alquimista', 'Paulo Coelho', 'Ficção', 1, '001'),
('1984', 'George Orwell', 'Distopia', 1, '002'),
('Dom Casmurro', 'Machado de Assis', 'Clássico', 1, '003'),
('A Revolução dos Bichos', 'George Orwell', 'Fábula', 1, '004'),
('O Pequeno Príncipe', 'Antoine de Saint-Exupéry', 'Infantil', 1, '005');

INSERT INTO usuario (nome, cpf, senha, email) VALUES
('Maria Silva', '123.456.789-00', '12345', 'maria@email.com'),
('João Santos', '987.654.321-00', '12345', 'joao@email.com'),
('Ana Oliveira', '111.222.333-44', '12345', 'ana@email.com'),
('Carlos Pereira', '555.666.777-88', '12345', 'carlos@email.com'),
('Fernanda Costa', '222.333.444-99', '12345', 'fernanda@email.com');

INSERT INTO emprestimo (id_livro,id_usuario,devolvido) VALUES (1, 2, FALSE);
INSERT INTO emprestimo (id_livro,id_usuario,devolvido) VALUES (3, 1, FALSE);

INSERT INTO emprestimo (id_livro,id_usuario,devolvido) VALUES (3, 4, FALSE);

-- select * from emprestimo where id_livro=3 order by id_emprestimo desc;