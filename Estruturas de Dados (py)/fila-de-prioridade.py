import sys

class Fila_Prioridade:
    def __init__(self):
        self.fila = []
        self.orgao = ""
        self.capacidade = 0
    
    def custom_pop(lst):
        if not lst:
            return None  
        last_element = lst[-1]
        lst[:] = lst[:-1]
        return last_element
    
    def vazia(self):
        return len(self.fila) == 0
    
    def heapify_down(self, index):
        while True:
            index_no_esquerda = 2 * index + 1
            index_no_direita = 2 * index + 2
            maior = index

            if (index_no_esquerda < len(self.fila) and self.fila[index_no_esquerda][1] > self.fila[maior][1]):
                maior = index_no_esquerda
            if (index_no_direita < len(self.fila) and self.fila[index_no_direita][1] > self.fila[maior][1]):
                maior = index_no_direita
            
            if maior != index:
                self.fila[index], self.fila[maior] = self.fila[maior], self.fila[index]
                index = maior
            else:
                break
    
    def heapify_up(self, index):
        while index > 0:
            pai_index = (index - 1)//2
            if self.fila[index][1] > self.fila[pai_index][1]:
                self.fila[index], self.fila[pai_index] = self.fila[pai_index], self.fila[index]
                index = pai_index
            else:
                break
    
    def push(self, pessoa, idade):
        self.fila.append((pessoa, idade))
        self.heapify_up((len(self.fila) - 1))
    
    def pull(self):
        if len(self.fila) == 0:
            return None
        
        if len(self.fila) == 1:
            return Fila_Prioridade.custom_pop(self.fila)

        valor_max = self.fila[0]
        self.fila[0] = Fila_Prioridade.custom_pop(self.fila)
        self.heapify_down(0)

        return valor_max


def main(args):

    print("Quantidade de argumentos (len(args)): " + str(len(args)))
    for i, arg in enumerate(args):
        print("Argumento " + str(i) + " (args[" + str(i) + "]): " + arg)

    input = open(sys.argv[1], "r")
    output = open(sys.argv[2], "w")

    lista_input = input.read().splitlines()
    num_org = int(lista_input[0])

    cont = 1
    while cont <= num_org:
        orgao = Fila_Prioridade()
        entrada = lista_input[cont].slit(" ")
        orgao.orgao = entrada[0]
        orgao.capacidade = int(entrada[1])
        cont += 1
    
    lista_input = lista_input[cont:]
    num_pessoa = int(lista_input[0])

    cont1 = 1
    while cont1 < num_pessoa:
        entrada = lista_input[cont].split("|")
        
    






if __name__ == '__main__':
    main(sys.argv)