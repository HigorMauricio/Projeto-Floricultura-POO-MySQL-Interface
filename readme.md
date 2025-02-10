# Projeto Floricultura
## POO em Python + Interface Gráfica + MySQL

O seguinte programa representa um "app" para utilização do dono(a) de uma floricultura. Nele, a pessoa pode: 
- adicionar flores ao estoque (Banco de Dados), após realizar uma compra de produtos. Informando o nome, cor e quantidade;
- Criar um buque para algum cliente, a partir das opçoes de flores presentes no Banco de Dados e a removendo após a escolha; 
- Visualizar e deletar alguma flor no buque, fazendo com que essa flor volte a ficar diponível no Banco de Dados;
- Visualizar e deletar flores dispóniveis, em caso de alguma adição errada.

## Estrutra do Banco de dados(MySQL):
- Database: floriculturadados
- Tabela: flores
- Colunas: NOME e COR

Exemplo:


![Image](https://github.com/user-attachments/assets/50127e64-e847-415e-bb5e-f624bc62e692)


## Banco.py
    É a responsável por linterligar o Banco de Dados MySQL ao Python. Esse arquivos tem 5 funções (def):
    - Biblioteca Utilizada: mysql.connector

1. criar_conexão: 

    Cria e retorna a conexão com o banco de dados.

2. fechar_conexão:

    Ensera a conexão com o banco de dados.

3. inserir_dados:

    Insere dados ao banco de dados.

        ('insert into flores (nome, cor) values (%s, %s))

4. deletar_dados:

    Deleta dados do banco de dados.

        ('delete from flores where nome=%s and cor=%s limit 1')

5. mostrar_flores:
    
    seleciona todos os itens do banco de dados.

        ('select * from flores order by nome, flor')

## Floricultura.py
### Classe Floricultura:
    Resposável por criar as funcionalidades da floricultura, a partir de 3 funções(def):


1. add_flores:

    Chama a função inserir_dados do banco.py e passa o nome e cor dos valores a serem adicionados.

2. make_buque:

    Adiciona a informação nome e cor a uma lista chamada buque.

3. remove_from_buque:

    Remove uma flor do buque, a partir do nome e cor passado, e o retorna ao banco de dados pela função inserir_dados do banco.py.

## Final.py

    É a responsável pela criação da interface gráfica e união dos outros dos arquivos.
    - Biblioteca utilizadas: tkinter e PIL

### Tela Inicial:

![Image](https://github.com/user-attachments/assets/201e87a6-1842-42e4-8655-9dad951f457c)

### Adicionar Flores:

![Image](https://github.com/user-attachments/assets/4791846a-2e51-48f3-82bf-af22b15cedc2)

*o valor 1 em qtd vem como padrão*

### Criar Buque:

![Image](https://github.com/user-attachments/assets/b2c1f05a-3b0c-4cc3-8679-46641d4be758)

### Visualizar Buque:

![Image](https://github.com/user-attachments/assets/b0374a6f-d220-47d7-ba1f-40237715e30e)

### Flores Disponíveis:

![Image](https://github.com/user-attachments/assets/f42661b8-3131-4a1b-9541-12e526d26293)

*Desing feito em colaboração com a minha namorada, Lara Melisa, muito obrigado pela ajuda. ❤️*
