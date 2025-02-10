from banco import inserir_dados
   
class Floricultura:
    def __init__(self):
        self.buque = []

    def add_flores(self, nome, cor):
        inserir_dados(nome, cor)

    def make_buque(self, nome, cor):
        self.buque.append([nome, cor])

    def remove_from_buque(self, nome, cor):
        for posição, flor in enumerate(self.buque):
            print('chegou ate aqui')
            if flor[0] == nome:
                print('passou do primeiro if')
                print(flor[0], nome)
                print(flor[1], cor)
                if flor[1] == cor:
                    print('passou do segundo if')
                    print(posição)
                    self.buque.pop(posição)
                    inserir_dados(nome, cor)
                    return 


