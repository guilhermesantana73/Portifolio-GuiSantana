import sys

class No:
    def __init__(self, nome):
        self.nome = nome
        self.proximo = None
        self.anterior = None
    
class ListaDuplamenteEncadeada:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def __lista_vazia(self):
        return self.primeiro == None
    
    def inserir(self, nome):
        novo = No(nome)
        if self.__lista_vazia():
            self.primeiro = novo
            self.ultimo = novo
        else:
            novo.anterior = self.ultimo
            self.ultimo.proximo = novo
            self.ultimo = novo
    
    def remover(self, nome):
        atual = self.primeiro
        while atual.nome != nome:
            atual = atual.proximo
            if atual == None:
                return None
        if atual == self.primeiro:
            self.primeiro = atual.proximo
        else:
            atual.anterior.proximo = atual.proximo
        
        if atual == self.ultimo:
            self.ultimo = atual.anterior
        else:
            atual.proximo.anterior = atual.anterior
        return atual

    def pesquisa(self, nome):
        atual = self.primeiro
        while atual:
            if atual.nome == nome:
               return True
            atual = atual.proximo
        return None
    
    def visualizar(self, nome):
        atual = self.primeiro
        while atual:
            if atual.nome == nome:
                if atual == self.primeiro and atual.proximo == None:
                    return (f"[ OK  ] {self.primeiro.nome}<-{self.primeiro.nome}->{self.primeiro.nome}")
                if atual == self.primeiro:
                    return (f"[ OK  ] {self.ultimo.nome}<-{self.primeiro.nome}->{self.primeiro.proximo.nome}")
                elif atual == self.ultimo:
                    return (f"[ OK  ] {atual.anterior.nome}<-{self.ultimo.nome}->{self.primeiro.nome}")
                else:
                    return (f"[ OK  ] {atual.anterior.nome}<-{atual.nome}->{atual.proximo.nome}")
            atual = atual.proximo


def main(args):

    print("Quantidade de argumentos (len(args)): " + str(len(args)))
    for i, arg in enumerate(args):
        print("Argumento " + str(i) + " (args[" + str(i) + "]): " + arg)

    input = open(sys.argv[1], "r")
    global output
    output = open(sys.argv[2], "w")

    redesocial = ListaDuplamenteEncadeada()
    redesocial_input = input.read()
    lista_input = redesocial_input.split("\n")
    c = 0

    while c < len(lista_input):
        entrada = lista_input[c].split(" ")
        op = entrada[0]
        temp = entrada[1:]
        user = ""
        cont = 0
        while cont < len(temp):
            user = user + str(temp[cont]) + " "
            cont += 1
        user = user[:-1]
        pesquisa = redesocial.pesquisa(user)
        
        if op == "ADD":
            if pesquisa == None:
                redesocial.inserir(user)
                output.write(f"[ OK  ] {op} {user}\n")
            else:
                output.write(f"[ERROR] {op} {user}\n")
        if op == "SHOW":
            if pesquisa == None:
                output.write(f"[ERROR] ?<-{user}->?\n")
            else:
                view = redesocial.visualizar(user)
                output.write(f"{view}\n")
        if op == "REMOVE":
            if pesquisa == None:
                output.write(f"[ERROR] {op} {user}\n")
            else:
                redesocial.remover(user)
                output.write(f"[ OK  ] {op} {user}\n")
        c += 1

    input.close()
    output.close()


# Executando a funcao main
if __name__ == '__main__':
    # Passando os argumentos do programa
    main(sys.argv)