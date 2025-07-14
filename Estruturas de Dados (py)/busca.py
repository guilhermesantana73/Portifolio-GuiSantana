import sys

class No:
    def __init__(self, palavra):
        self.palavra = palavra #nessa arvore temos a palavra (chave do no), os sinonimos, o valor do balanceamento individual de cada no
        self.sinonimos = list() #os sinonimos é uma lista, é so fazer um processo similar ao da classe Notebook
        self.tamanho = 0
        self.altura = 1
        self.esquerda = None
        self.direita = None
    
    def mostrar_No(self):
        print(self.palavra)
        for i in self.sinonimos:
            print(i)
    
    def add_sinonimo(self, lista):
        for i in lista:
            self.sinonimos.append(i)

    def show_sinonimo(self):
        tam = int(self.tamanho)
        if tam == 0:
            output.write("-\n")
        if tam == 1:
            output.write(f"{self.sinonimos[0]}\n")
        if tam == 2:
            output.write(f"{self.sinonimos[0]},{self.sinonimos[1]}\n")
        if tam == 3:
            output.write(f"{self.sinonimos[0]},{self.sinonimos[1]},{self.sinonimos[2]}\n")
        if tam == 4:
            output.write(f"{self.sinonimos[0]},{self.sinonimos[1]},{self.sinonimos[2]},{self.sinonimos[3]}\n")
        if tam == 5:
            output.write(f"{self.sinonimos[0]},{self.sinonimos[1]},{self.sinonimos[2]},{self.sinonimos[3]},{self.sinonimos[4]}\n")
        if tam == 6:
            output.write(f"{self.sinonimos[0]},{self.sinonimos[1]},{self.sinonimos[2]},{self.sinonimos[3]},{self.sinonimos[4]},{self.sinonimos[5]}\n")
        if tam == 7:
            output.write(f"{self.sinonimos[0]},{self.sinonimos[1]},{self.sinonimos[2]},{self.sinonimos[3]},{self.sinonimos[4]},{self.sinonimos[5]},{self.sinonimos[6]}\n")
        if tam == 8: 
            output.write(f"{self.sinonimos[0]},{self.sinonimos[1]},{self.sinonimos[2]},{self.sinonimos[3]},{self.sinonimos[4]},{self.sinonimos[5]},{self.sinonimos[6]},{self.sinonimos[7]}\n")
        if tam == 9:
            output.write(f"{self.sinonimos[0]},{self.sinonimos[1]},{self.sinonimos[2]},{self.sinonimos[3]},{self.sinonimos[4]},{self.sinonimos[5]},{self.sinonimos[6]},{self.sinonimos[7]},{self.sinonimos[8]}\n")
        if tam == 10:
            output.write(f"{self.sinonimos[0]},{self.sinonimos[1]},{self.sinonimos[2]},{self.sinonimos[3]},{self.sinonimos[4]},{self.sinonimos[5]},{self.sinonimos[6]},{self.sinonimos[7]},{self.sinonimos[8]},{self.sinonimos[9]}\n")

class Arvore_AVL:
    def __init__(self):
        self.raiz = None

    def get_altura(self, no):
        if not no:
            return 0

        return no.altura
    
    def get_balance(self, no):
        if not no:
            return 0
        
        return self.get_altura(no.esquerda) - self.get_altura(no.direita)
    
    def rotacao_esquerda(self, no):
        eixo = no.direita
        no.direita = eixo.esquerda
        eixo.esquerda = no

        #Dando update e fazendo o rebalanceamento de cada no
        no.altura = 1 + max(self.get_altura(no.esquerda), self.get_altura(no.direita))
        eixo.altura = 1 + max(self.get_altura(eixo.esquerda), self.get_altura(eixo.direita))

        return eixo #retornando a nova raiz
    
    def rotacao_direita(self, no):
        eixo = no.esquerda
        no.esquerda = eixo.direita
        eixo.direita = no
       
        #Dando update e fazendo o rebalanceamento de cada no
        no.altura = 1 + max(self.get_altura(no.esquerda), self.get_altura(no.direita))
        eixo.altura = 1 + max(self.get_altura(eixo.esquerda), self.get_altura(eixo.direita))

        return eixo #retornando a nova raiz
    
    def rotacao_esquerda_direita(self, no):
        if no.esquerda is None:
            return no
        esquerda = no.esquerda
        no.esquerda = self.rotacao_esquerda(esquerda)
        return self.rotacao_direita(no)

    def rotacao_direita_esquerda(self, no):
        if no.direita is None:
            return no
        direita = no.direita
        no.direita = self.rotacao_direita(direita)
        return self.rotacao_esquerda(no)

    def balanceamento(self, no):
        fb = self.get_balance(no)
        if fb == 2:
            if no.esquerda is not None and self.get_balance(no.esquerda) == -1:
                return self.rotacao_esquerda_direita(no)
            else:
                return self.rotacao_direita(no)
        elif fb == -2:
            if no.direita is not None and self.get_balance(no.direita) == 1:
                return self.rotacao_direita_esquerda(no)
            else:
                return self.rotacao_esquerda(no)
        else:
            return no

    def _insere(self, no, palavra, sinonimos, tamanho):
        if no is None:
            novo = No(palavra)
            novo.add_sinonimo(sinonimos)
            novo.tamanho = tamanho
            return novo
        elif palavra < no.palavra:
            no.esquerda = self._insere(no.esquerda, palavra, sinonimos, tamanho)
        else:
            no.direita = self._insere(no.direita, palavra, sinonimos, tamanho)

        no_balanceado = self.balanceamento(no)
        no_balanceado.altura = 1 + max(self.get_altura(no_balanceado.esquerda), self.get_altura(no_balanceado.direita))
        
        return no_balanceado

    def inserir(self, palavra, sinonimos, tamanho):
        self.raiz = self._insere(self.raiz, palavra, sinonimos, tamanho)
                
    def pesquisar(self, palavra):
        atual = self.raiz
        while atual:
            if palavra == atual.palavra:
                return atual
            elif palavra < atual.palavra:
                atual = atual.esquerda
            else:
                atual = atual.direita
        return None 
    
    def caminho(self, palavra):
        atual = self.raiz
        caminho = []
        
        while atual != None and atual.palavra != palavra:
            caminho.append(str(atual.palavra)+"->")

            if palavra < atual.palavra:
                atual = atual.esquerda
            else:
                atual = atual.direita
        
        if atual == None:
            caminho.append("?")
        else:
            caminho.append(str(atual.palavra))
        
        return caminho
    
    def visualizar(self, palavra):
        string = ""
        view = self.caminho(palavra)
        tamanho = len(view)
        c = 0
        
        while c < tamanho:
            string = string + str(view[c]) 
            c += 1

        string = "[" + string + "]"

        return string

def main():
    '''
    print("Quantidade de argumentos (len(args)): " + str(len(args)))
    for i, arg in enumerate(args):
        print("Argumento " + str(i) + " (args[" + str(i) + "]): " + arg)'''

    input = open("teste1.txt", "r")
    global output
    output = open("teste3.txt", "w")

    dicionario = Arvore_AVL()
    arquivos_input = input.read()
    lista_input = arquivos_input.split("\n")
    num_entradas = int(lista_input[0])
    contador_in = 1

    while contador_in <= num_entradas:
        entrada = lista_input[contador_in].split(" ")
        palavra = str(entrada[0])
        qtd_sinonimos = int(entrada[1])
        resto = entrada[2:]
        raiz = dicionario.inserir(palavra, resto, qtd_sinonimos)
        contador_in += 1

    num_busca = int(lista_input[contador_in])
    contador_sc = 1
    contador_in = contador_in + 1

    while contador_sc <= num_busca:
        entrada = str(lista_input[contador_in])
        pesquisa = dicionario.pesquisar(entrada)
        if pesquisa != None:
            output.write(f"{dicionario.visualizar(entrada)}\n")
            pesquisa.show_sinonimo()
        else:
            output.write(f"{dicionario.visualizar(entrada)}\n")
            output.write("-\n")
        contador_in += 1
        contador_sc += 1
    
    input.close()
    output.close()


# Executando a funcao main
if __name__ == '__main__':
    # Passando os argumentos do programa
    main()