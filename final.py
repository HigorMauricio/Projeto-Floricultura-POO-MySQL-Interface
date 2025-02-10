from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from floricultura import Floricultura
import banco

#chamando a classe floricultura
floricultura = Floricultura()

#def sair
def fechar_janela(janela):
    janela.destroy()

def popular(tabela):
        tabela.delete(*tabela.get_children())
        linhas = banco.mostarar_flores()
        for i in linhas:
            tabela.insert('', 'end', values=i)
    
#janela de adição de flores
def add_flor():
    global nome, cor, text_confirmação, i
    i = 1
    #pegar os valores e adicionar no banco de dados
    def get_values():
        global i
        qtd_valor = int(qtd.get())
        nome_valor = nome.get().upper()
        cor_valor = cor.get().upper()
        if nome_valor and cor_valor != '':
            for c in range(0, qtd_valor):
                floricultura.add_flores(nome_valor, cor_valor)
                text_confirmação['text'] = f'{i} Adição(ões) completa(s)'
                i +=1
        else: 
            fechar_janela(janela_add_flor)
            messagebox.showinfo(title='ERRO FALTA DE VALOR', message='Existe algum dado faltando')
        
            
    #criação da janela
    janela_add_flor = Toplevel(janela)
    janela_add_flor.attributes("-fullscreen", True)

    #criação do canva
    canva_janela_add = Canvas(janela_add_flor, height=1080, width=1920)
    canva_janela_add.pack(side=LEFT, expand=True, fill=BOTH)
    canva_janela_add.config(bg='#ebe1d7')

    #adição do fundo
    fundo = Image.open(r'C:\Users\Higor\Documents\Vscode\Aprendendo Python POO\Floricultura\imagens\projeto floricultura.png')
    fundo = fundo.resize((1360, 770), Image.LANCZOS)
    fundo_tk = ImageTk.PhotoImage(fundo)
    canva_janela_add.create_image(0,0, anchor= 'nw', image=fundo_tk)

    #adição das entrys
    nome = Entry(janela_add_flor, bg='#96a396', bd=0, font=('rockwell', 12))
    nome.place(x=320,y=235)
    cor = Entry(janela_add_flor,bg='#96a396', bd=0, font=('rockwell', 12))
    cor.place(x=320,y=327)
    str1 = IntVar(value=1)
    qtd = Entry(janela_add_flor,bg='#96a396', bd=0, font=('rockwell', 12), textvariable=str1)
    qtd.place(x=320, y=418)

    #adição do botao de confirmação
    imagem_botao_add = Image.open(r'C:\Users\Higor\Documents\Vscode\Aprendendo Python POO\Floricultura\imagens\Captura de tela 2025-02-05 213625.png')
    imagem_botao_add = imagem_botao_add.resize((130, 67), Image.LANCZOS)
    imagem_botao_add_tk = ImageTk.PhotoImage(imagem_botao_add)
    botao = Button(janela_add_flor, image=imagem_botao_add_tk, command=get_values, bd=0, highlightthickness=0, bg='#ebe1d7', activebackground='#ebe1d7' )
    botao.place(x=580, y=500)

    #texto informando a confirmação
    text_confirmação = Label(janela_add_flor, text='', bg='#ebe1d7', font=('rockwell', 12), foreground='Forest Green')
    text_confirmação.place(x=400, y=470)

    #botao de sair
    botao_sair = Button(janela_add_flor, image=imagem_botao_sair_tk, command=lambda: fechar_janela(janela_add_flor),bd=0, highlightthickness=0, bg='#ebe1d7', activebackground='#ebe1d7' ).place(y=700, x=700)

    janela_add_flor.mainloop()

#janela de adicionar flores ao buque
def make_buque():

    #selecionar informações da treevie e remove-la do banco de dados
    def get_buque():
        flor_codigo = tabela1.selection()
        for flor in flor_codigo:
            flor_selecionada = tabela1.item(flor, 'values')
            nome = flor_selecionada[0]
            cor = flor_selecionada[1]
            floricultura.make_buque(nome, cor)
            banco.deletar_dados(nome, cor)
        popular(tabela1)

    #criação da janela
    janela_make_buque = Toplevel(janela)
    janela_make_buque.attributes("-fullscreen", True)
    janela_make_buque.config(bg='#ebe1d7')

    #criação do canva
    canva_make_buque = Canvas(janela_make_buque, height=1080, width=1920)
    canva_make_buque.pack(side=LEFT, expand=True, fill=BOTH)
    canva_make_buque.config(bg='#ebe1d7')

    #adição da imagem de fundo
    fundo = Image.open(r'C:\Users\Higor\Documents\Vscode\Aprendendo Python POO\Floricultura\imagens\tela_buque.png')
    fundo = fundo.resize((1360, 770), Image.LANCZOS)
    fundo_tk = ImageTk.PhotoImage(fundo)
    canva_make_buque.create_image(0,0, anchor= 'nw', image=fundo_tk)

    #criação do treeview
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("Treeview", background="#96a396", fieldbackground='#96a396', highlightthickness=0, bd=0, rowheight=50)
    style.map('Treeview', background=[('selected', '#2f4858')])

    tabela_frame = Frame(janela_make_buque)
    tabela_frame.place(x=90, y=150)

    tabela_scroll = Scrollbar(tabela_frame)
    tabela_scroll.pack(side=RIGHT, fill=Y)

    tabela1 = ttk.Treeview(tabela_frame, columns=('NOME', 'COR'), show='headings', yscrollcommand=tabela_scroll.set)
    tabela1.column('NOME', minwidth=0, width=250)
    tabela1.column('COR', minwidth=0, width=250)
    tabela1.heading('NOME', text='NOME')
    tabela1.heading('COR', text='COR')
    tabela1.pack()
    popular(tabela1)

    tabela_scroll.config(command=tabela1.yview)

    #criação do botao de confirmação
    imagem_botao_selecionar = Image.open(r'C:\Users\Higor\Documents\Vscode\Aprendendo Python POO\Floricultura\imagens\botao-selecionar.png')
    imagem_botao_selecionar = imagem_botao_selecionar.resize((95, 47), Image.LANCZOS)
    imagem_botao_selecionar_tk = ImageTk.PhotoImage(imagem_botao_selecionar)
    botao_selecionar = Button(janela_make_buque, image=imagem_botao_selecionar_tk, command=get_buque, bd=0, highlightthickness=0, bg='#ebe1d7', activebackground='#ebe1d7')
    botao_selecionar.place(x=85, y=680)

    #adição do botao de sair
    botao_sair = Button(janela_make_buque, image=imagem_botao_sair_tk, command=lambda: fechar_janela(janela_make_buque),bd=0, highlightthickness=0, bg='#ebe1d7', activebackground='#ebe1d7')
    botao_sair.place(y=700, x=700)

    janela_make_buque.mainloop()

def visualizar():
    def deletar():
        def nova_entrada():
            tabela2.delete(*tabela2.get_children())
            for flor in floricultura.buque:
                tabela2.insert('', 'end', values=(flor[0], flor[1]))


        flor_codigo = tabela2.selection()
        for flor in flor_codigo:
            flor_selecionado = tabela2.item(flor, 'values')
            nome = flor_selecionado[0]
            cor = flor_selecionado[1]
            floricultura.remove_from_buque(nome, cor)
        nova_entrada()


    janela_visuzaliar = Toplevel(janela)
    janela_visuzaliar.attributes("-fullscreen", True)

    canva_visualizar = Canvas(janela_visuzaliar, height=1080, width=1920)
    canva_visualizar.pack(side=LEFT, expand=True, fill=BOTH)
    canva_visualizar.config(bg='#ebe1d7')

    fundo_visualizar = Image.open(r'C:\Users\Higor\Documents\Vscode\Aprendendo Python POO\Floricultura\imagens\tela-fundo-visu.png')
    fundo_visualizar = fundo_visualizar.resize((1360, 770), Image.LANCZOS)
    fundo_visualizar_tk = ImageTk.PhotoImage(fundo_visualizar)
    canva_visualizar.create_image(0,0, image=fundo_visualizar_tk, anchor='nw')

    style = ttk.Style()
    style.theme_use('clam')
    style.configure("Treeview", background="#96a396", fieldbackground='#96a396', highlightthickness=0, bd=0, rowheight=50)
    style.map('Treeview', background=[('selected', '#2f4858')])

    tabela_frame = Frame(janela_visuzaliar)
    tabela_frame.place(x=90, y=150)

    tabela_scroll = Scrollbar(tabela_frame)
    tabela_scroll.pack(side=RIGHT, fill=Y)

    tabela2 = ttk.Treeview(tabela_frame, columns=('NOME','COR'), show='headings', yscrollcommand=tabela_scroll.set)
    tabela2.column('NOME', minwidth=0, width=250)
    tabela2.column('COR', minwidth=0, width=250)
    tabela2.heading('NOME', text='NOME')
    tabela2.heading('COR', text='COR')
    tabela2.pack()

    for flor in floricultura.buque:
        tabela2.insert('', 'end', values=(flor[0], flor[1]))

    tabela_scroll.config(command=tabela2.yview)

    imagem_botao_deletar = Image.open(r'C:\Users\Higor\Documents\Vscode\Aprendendo Python POO\Floricultura\imagens\botao-deletar.png')
    imagem_botao_deletar = imagem_botao_deletar.resize((100, 35), Image.LANCZOS)
    imagem_botao_deletar_tk = ImageTk.PhotoImage(imagem_botao_deletar)
    botao_deletar = Button(janela_visuzaliar, image=imagem_botao_deletar_tk, command=deletar, bd=0, highlightthickness=0, bg='#ebe1d7', activebackground='#ebe1d7')
    botao_deletar.place(x=85, y=680)

    botao_sair = Button(janela_visuzaliar, image=imagem_botao_sair_tk, command=lambda: fechar_janela(janela_visuzaliar),bd=0, highlightthickness=0, bg='#ebe1d7', activebackground='#ebe1d7' ).place(y=700, x=700)

    janela_visuzaliar.mainloop()

def disp():
    def deletar():
        flor_codigo = tabela3.selection()
        for flor in flor_codigo:
            flor_selecionada = tabela3.item(flor, 'values')
            nome = flor_selecionada[0]
            cor = flor_selecionada[1]
            banco.deletar_dados(nome, cor)
        popular(tabela3)

    janela_disponivel = Toplevel(janela)
    janela_disponivel.attributes('-fullscreen', True,)

    canva_janela_disponivel = Canvas(janela_disponivel, bg='#ebe1d7', height=1080, width=1920)
    canva_janela_disponivel.pack(side=LEFT, expand=True, fill=BOTH)

    fundo_disp = Image.open(r'C:\Users\Higor\Documents\Vscode\Aprendendo Python POO\Floricultura\imagens\fundo-disp.png')
    fundo_disp = fundo_disp.resize((1360, 770), Image.LANCZOS)
    fundo_disp_tk = ImageTk.PhotoImage(fundo_disp)
    canva_janela_disponivel.create_image(0,0, image=fundo_disp_tk, anchor='nw')

    style = ttk.Style()
    style.theme_use('clam')
    style.configure("Treeview", background="#96a396", fieldbackground='#96a396', highlightthickness=0, bd=0, rowheight=50)
    style.map('Treeview', background=[('selected', '#2f4858')])

    tabela_frame = Frame(janela_disponivel)
    tabela_frame.place(x=90, y=150)

    tabela_scroll = Scrollbar(tabela_frame)
    tabela_scroll.pack(side=RIGHT, fill=Y)

    tabela3 = ttk.Treeview(tabela_frame, columns=('NOME','COR'), show='headings', yscrollcommand=tabela_scroll.set)
    tabela3.column('NOME', minwidth=0, width=250)
    tabela3.column('COR', minwidth=0, width=250)
    tabela3.heading('NOME', text='NOME')
    tabela3.heading('COR', text='COR')
    tabela3.pack()
    popular(tabela3)

    tabela_scroll.config(command=tabela3.yview)

    imagem_botao_deletar = Image.open(r'C:\Users\Higor\Documents\Vscode\Aprendendo Python POO\Floricultura\imagens\botao-deletar.png')
    imagem_botao_deletar = imagem_botao_deletar.resize((100, 35), Image.LANCZOS)
    imagem_botao_deletar_tk = ImageTk.PhotoImage(imagem_botao_deletar)
    botao_deletar = Button(janela_disponivel, image=imagem_botao_deletar_tk, command=deletar, bd=0, highlightthickness=0, bg='#ebe1d7', activebackground='#ebe1d7')
    botao_deletar.place(x=85, y=680)
    

    botao_sair = Button(janela_disponivel, image=imagem_botao_sair_tk, command=lambda: fechar_janela(janela_disponivel),bd=0, highlightthickness=0, bg='#ebe1d7', activebackground='#ebe1d7' ).place(y=700, x=700)

    janela_disponivel.mainloop()

#criando janela principal com fundo
janela = Tk()
janela.title('janela principal')
janela.attributes("-fullscreen", True)
canva = Canvas(janela, height=1080, width=1920)
canva.pack(side=LEFT, expand=True, fill=BOTH)
canva.config(bg='#ebe1d7')
fundo = Image.open(r'C:\Users\Higor\Documents\Vscode\Aprendendo Python POO\Floricultura\imagens\2.png')
fundo = fundo.resize((1360, 770), Image.LANCZOS)
fundo_tk = ImageTk.PhotoImage(fundo)
canva.create_image(0,0, anchor= 'nw', image=fundo_tk)

#Criando botões de adicionar flor
imagem_botao = Image.open(r'C:\Users\Higor\Documents\Vscode\Aprendendo Python POO\Floricultura\imagens\imagem.png')
imagem_botao = imagem_botao.resize((100, 50), Image.LANCZOS)
imagem_botao_tk = ImageTk.PhotoImage(imagem_botao)
botao_add_flor = Button(janela, image=imagem_botao_tk, command=add_flor, bd=0, highlightthickness=0, bg='#ebe1d7', activebackground='#ebe1d7')
botao_add_flor.place(x=365, y=45)

#criando botao de adicionar ao buque
imagem_botao_buque = Image.open(r'C:\Users\Higor\Documents\Vscode\Aprendendo Python POO\Floricultura\imagens\imagem-botao-buque.png')
imagem_botao_buque = imagem_botao_buque.resize((110, 45), Image.LANCZOS)
imagem_botao_buque_tk = ImageTk.PhotoImage(imagem_botao_buque)
botao_make_buque = Button(janela, image=imagem_botao_buque_tk, command=make_buque, bd=0, highlightthickness=0, bg='#ebe1d7', activebackground='#ebe1d7')
botao_make_buque.place(x=495, y=50)

#criando botao de visualizar buque
imagem_botao_visu = Image.open(r'C:\Users\Higor\Documents\Vscode\Aprendendo Python POO\Floricultura\imagens\botao-visu.png')
imagem_botao_visu = imagem_botao_visu.resize((100, 45), Image.LANCZOS)
imagem_botao_visu_tk = ImageTk.PhotoImage(imagem_botao_visu)
botao_visu = Button(janela, image= imagem_botao_visu_tk, command=visualizar, bd=0, highlightthickness=0, bg='#ebe1d7', activebackground='#ebe1d7')
botao_visu.place(x=645, y=50)

#criando botao de visualizar flores disponiveis
imagem_botao_disp = Image.open(r'C:\Users\Higor\Documents\Vscode\Aprendendo Python POO\Floricultura\imagens\botao-flores-disp.png')
imagem_botao_disp = imagem_botao_disp.resize((112, 55), Image.LANCZOS)
imagem_botao_disp_tk = ImageTk.PhotoImage(imagem_botao_disp)
botao_disp = Button(janela, image=imagem_botao_disp_tk, command=disp, bd=0, highlightthickness=0, bg='#ebe1d7', activebackground='#ebe1d7')
botao_disp.place(x=785, y=50)

#criando botao de sair
imagem_botao_sair = Image.open(r'C:\Users\Higor\Documents\Vscode\Aprendendo Python POO\Floricultura\imagens\botao-sair.png')
imagem_botao_sair = imagem_botao_sair.resize((90, 50), Image.LANCZOS)
imagem_botao_sair_tk = ImageTk.PhotoImage(imagem_botao_sair)
botao_sair = Button(janela, image=imagem_botao_sair_tk, command=lambda: fechar_janela(janela),bd=0, highlightthickness=0, bg='#ebe1d7', activebackground='#ebe1d7' )
botao_sair.place(y=50, x=925)

janela.mainloop()

