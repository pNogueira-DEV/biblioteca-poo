class ItemBiblioteca:
    def __init__(self, codigo, titulo,ano):
        self.set_codigo(codigo)
        self.set_titulo(titulo)
        self.set_ano(ano)
        self.__disponivel = True

