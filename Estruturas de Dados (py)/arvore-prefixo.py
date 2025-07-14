import sys
import cProfile
import timeit

class No:
    def __init__(self, char):
        self.char = char
        self.fim = False
        self.filhos = {}

class Arvore_Prefixo:
    def __init__(self):
        self.raiz = No("")
    
    def custom_pop(lst):
        if len(lst) == 0:
            return None  
        last_element = lst[-1]
        del lst[-1] 
        return last_element
    
    def inserir(self, palavra):
        no = self.raiz

        for char in palavra:
            if char in no.filhos:
                no = no.filhos[char]
            else:
                novo = No(char)
                no.filhos[char] = novo
                no = novo
        
        no.fim = True

    def view(self, no, prefixo, lista):
        pilha = [(no, prefixo)]
        while pilha:
            no_atual, pref_atual = Arvore_Prefixo.custom_pop(pilha)
            if no_atual.fim:
                lista.append(pref_atual)
            
            for char, no_filho in no_atual.filhos.items():
                pilha.append((no_filho, pref_atual + char))
        
    def pesquisa(self, x):
        self.lista = []
        no = self.raiz

        for char in x:
            if char in no.filhos:
                no = no.filhos[char]
            else:
                return None
        
        self.view(no, x, self.lista)

        return self.lista
    

def main(args):
    
    print("Quantidade de argumentos (len(args)): " + str(len(args)))
    for i, arg in enumerate(args):
        print("Argumento " + str(i) + " (args[" + str(i) + "]): " + arg)

    with open(sys.argv[1], "r") as input:
        api = Arvore_Prefixo()
        lista_input = input.read().split("\n")
        n = int(lista_input[0])
        c = 1

        while c <= n:
            palavra = lista_input[c]
            api.inserir(palavra)
            c += 1
        
        lista_input = lista_input[c:]
        x = int(lista_input[0])
        cont = 1

        with open(sys.argv[2], "w") as output:
            while cont <= x:
                palavra = lista_input[cont]
                if len(palavra) <= 4:
                    search = api.pesquisa(palavra)
                else:
                    prefixo = palavra[:len(palavra)//2]
                    search = api.pesquisa(prefixo)
                if search is None:
                    output.write(f"{palavra}:-\n")
                else:
                    search = ",".join(search)
                    output.write(f"{palavra}:{search}\n")
                cont += 1
    

if __name__ == '__main__':
    main(sys.argv)


'''
#cProfile.run("main(sys.argv)") -> esse é o jeito mais simples, mas que passa por todas as funções e te diz quantas vezes elas são chamadas!

print(timeit.timeit("main(sys.argv)", number=400, globals=globals())) -> esse, é outra maneira, que é testando o tempo, ele vai rodar a função com o caso base a quantidade
de vezes que a pessoa queira e no final vai dizer quanto tempo demorou. Pra esse teste em específico (loop de 400 vezes), a media de tempo da minha maquina foi 1.1 a 1.3 segundos.
mas pela minhas pesquisas, é algo mais arbitrário e depende muito de como a maquina vai rodar, então talvez seja mais impreciso! 
'''