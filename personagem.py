class Personagem:
    def __init__(self):
        self.dormindo = True
        self.sujo = True
        self.fome = True
        self.dinheiro = 0
        self.salario = 50
    


    def __str__(self):
        return "O personagem está  " + ("dormindo"  if self.dormindo else  "acordado")+" ,  " + ("sujo " if self.sujo else "limpo ")+"e "+("com fome" if self.fome else " sem fome")
    
