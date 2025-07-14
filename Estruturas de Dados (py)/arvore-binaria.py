import sys

class No:
    def __init__(self, nome, tipo, tamanho):
        self.nome = nome
        self.tipo = tipo
        self.tamanho = tamanho
        self.indice = None
        self.direita = None
        self.esquerda = None
    
    def mostrar_No(self):
        print(f'{self.indice} {self.nome} {self.tipo} {self.tamanho} bytes')

class Arvore_Binaria:
    def __init__(self):
        self.raiz = None
        self.cont_indice = 0
    
    def pesquisar(self, nome):
        atual = self.raiz
        while atual:
            if nome == atual.nome:
                return atual
            elif nome < atual.nome:
                atual = atual.esquerda
            else:
                atual = atual.direita
        return None
     
    def inserir(self, nome, tipo, tamanho):
        novo = No(nome, tipo, tamanho)
        novo.indice = self.cont_indice
        self.cont_indice += 1
        
        #Se a árvore estiver vazia 
        if self.raiz == None:
            self.raiz = novo
        else:
            atual = self.raiz
            while True:
                pai = atual
                #Esquerda 
                if nome < atual.nome:
                    atual = atual.esquerda
                    if atual == None:
                        pai.esquerda = novo
                        return 
                #Direita
                else:
                    atual = atual.direita
                    if atual == None:
                        pai.direita = novo
                        return
    
    def substituir(self, velho_nome, novo_nome, novo_tipo, novo_tamanho):
        no = self.pesquisar(velho_nome)
        if no and no.tipo == 'rw':
            no.nome = novo_nome
            no.tipo = novo_tipo
            no.tamanho = novo_tamanho
            no.indice = self.cont_indice
        else:
            self.inserir(novo_nome, novo_tipo, novo_tamanho)

    def em_ordem(self, no): #EPD
        if no != None:
            self.em_ordem(no.esquerda) #esquerda
            if no.tamanho == 1:
               output.write(f'{no.indice} {no.nome} {no.tipo} {no.tamanho} byte\n') #pai
            else:
                output.write(f'{no.indice} {no.nome} {no.tipo} {no.tamanho} bytes\n')
            self.em_ordem(no.direita) #direita
    
    def pre_ordem(self, no): #PED
        if no != None:
            if no.tamanho == 1:
                output.write(f'{no.indice} {no.nome} {no.tipo} {no.tamanho} byte\n') #pai
            else:
                output.write(f'{no.indice} {no.nome} {no.tipo} {no.tamanho} bytes\n')
            self.pre_ordem(no.esquerda) #esquerda
            self.pre_ordem(no.direita) #direita
    
    def pos_ordem(self, no): #EDP
        if no != None:
            self.pos_ordem(no.esquerda) #esquerda
            self.pos_ordem(no.direita) #direita
            if no.tamanho == 1:
                output.write(f'{no.indice} {no.nome} {no.tipo} {no.tamanho} byte\n') #pai
            else:
                output.write(f'{no.indice} {no.nome} {no.tipo} {no.tamanho} bytes\n')


def main_function(num):
    arquivos = Arvore_Binaria()
    contador = 0
    while contador < num:
        entrada = input().split()
        nome = str(entrada[0])
        tipo = str(entrada[1])
        tamanho = int(entrada[2])
        pesquisa = arquivos.pesquisar(nome)
        if pesquisa != None:
            arquivos.substituir(nome, nome, tipo, tamanho)
        else:
            arquivos.inserir(nome, tipo, tamanho)
        contador += 1

    print('EPD')
    arquivos.em_ordem(arquivos.raiz)
    print('PED')
    arquivos.pre_ordem(arquivos.raiz)
    print('EDP')
    arquivos.pos_ordem(arquivos.raiz)


def main(args):
    
    print("Quantidade de argumentos (len(args)): " + str(len(args)))
    for i, arg in enumerate(args):
        print("Argumento " + str(i) + " (args[" + str(i) + "]): " + arg)
    
    input = open(sys.argv[1], "r")
    global output
    output = open(sys.argv[2], "w")
    
    
    arquivos = Arvore_Binaria()
    arquivos_input = input.read()
    lista_input = arquivos_input.split("\n")
    num_entradas = int(lista_input[0])
    contador = 1

    while contador <= num_entradas:
        entrada = lista_input[contador].split(" ")
        nome = str(entrada[0])
        tipo = str(entrada[1])
        tamanho = int(entrada[2])
        pesquisa = arquivos.pesquisar(nome)
        if pesquisa != None:
            arquivos.substituir(nome, nome, tipo, tamanho)
        else:
            arquivos.inserir(nome, tipo, tamanho)
        contador += 1
    
    output.write("EPD\n")
    arquivos.em_ordem(arquivos.raiz)
    output.write("PED\n")
    arquivos.pre_ordem(arquivos.raiz)
    output.write("EDP\n")
    arquivos.pos_ordem(arquivos.raiz)


    input.close()
    output.close()



# Executando a funcao main
if __name__ == '__main__':
    # Passando os argumentos do programa
    main(sys.argv)