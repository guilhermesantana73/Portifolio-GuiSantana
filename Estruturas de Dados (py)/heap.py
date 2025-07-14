import sys
import cProfile

class Aposta:
    def __init__(self):
        self.codigo = ""
        self.numeros = []
        self.contador = 0

    def comparar(self, lst):
        for num in self.numeros:
            if num in lst:
                self.contador += 1


#Heap Maximo
def max_heapify(lst, index):
    index_esquerda = 2*index + 1
    index_direita = 2*index + 2

    if index_esquerda < len(lst) and lst[index_esquerda].contador > lst[index].contador:
        maior = index_esquerda
    else:
        maior = index
    
    if index_direita < len(lst) and lst[index_direita].contador > lst[maior].contador:
        maior = index_direita
    if maior != index:
        lst[index], lst[maior] = lst[maior], lst[index]
        max_heapify(lst, maior)

def heap_Max(lst):
    n = int((len(lst)//2)-1)
    for k in range(n,-1,-1):
        max_heapify(lst, k)

def extrair_max(lst):
    if len(lst) == 0:
        return 0
    
    if len(lst) == 1:
        valor_max = lst[0]
        del lst[0]
        return valor_max
        
    valor_max = lst[0]
    del lst[0]
    max_heapify(lst, 0)

    return valor_max


#Heap Minimo
def min_heapify(lst, index):
    index_esquerda = 2*index + 1
    index_direita = 2*index + 2

    if index_esquerda < len(lst) and lst[index_esquerda].contador < lst[index].contador:
        menor = index_esquerda
    else:
        menor = index
    
    if index_direita < len(lst) and lst[index_direita].contador < lst[menor].contador:
        menor = index_direita
    if menor != index:
        lst[index], lst[menor] = lst[menor], lst[index]
        min_heapify(lst, menor)

def heap_Min(lst):
    n = int((len(lst)//2)-1)
    for k in range(n,-1,-1):
        min_heapify(lst, k)

def extrair_min(lst):
    if len(lst) == 0:
        return 0
    
    if len(lst) == 1:
        valor_min = lst[0]
        del lst[0]
        return valor_min
        
    valor_min = lst[0]
    del lst[0]
    min_heapify(lst, 0)

    return valor_min


def main(args):

    print("Quantidade de argumentos (len(args)): " + str(len(args)))
    for i, arg in enumerate(args):
        print("Argumento " + str(i) + " (args[" + str(i) + "]): " + arg)

    with open(sys.argv[1], "r") as input_file, open(sys.argv[2], "w") as output_file:
        lista_input = input_file.read().splitlines()
        premio = int(lista_input[0])
        num_apostas = int(lista_input[1])
        sorteio = lista_input[2].split(" ")

        apostas = lista_input[3:]

        list_max = []
        list_min = []

        cont = 0
        while cont < num_apostas:
            total = apostas[cont].split(" ")
            aposta = Aposta()
            aposta.codigo = total[0]
            aposta.numeros = total[1:]

            aposta.comparar(sorteio)

            list_max.append(aposta)
            list_min.append(aposta)

            cont += 1
        

        premio = premio / 2
        
        heap_Max(list_max)

        cont1 = 0
        v_max = 1
        varA = extrair_max(list_max)
        varL = [varA]

        while cont1 < num_apostas:
            var1 = extrair_max(list_max)
            p = var1.contador
            var2 = extrair_max(list_max)
            q = var2.contador

            if p == q:
                v_max += 2
                varL.append(var1)
                varL.append(var2)
            else:
                if p != varL[0].contador:
                    break
                v_max += 1
                varL.append(var1)
                break
            cont1 += 1
        
        output_file.write(f"[{v_max}:{varL[0].contador}:{int(premio / v_max)}]\n")
        for var in varL:
            output_file.write(f"{var.codigo}\n")
        
        heap_Min(list_min)

        cont2 = 0
        v_min = 1
        varB = extrair_min(list_min)
        varK = [varB]

        while cont2 < num_apostas:
            var3 = extrair_min(list_min)
            r = var3.contador
            var4 = extrair_min(list_min)
            s = var4.contador

            if r == s:
                v_min += 2
                varK.append(var3)
                varK.append(var4)
            else:
                if r != varK[0].contador:
                    break
                v_min += 1
                varK.append(var3)
                break
            cont2 += 1

        output_file.write(f"[{v_min}:{varK[0].contador}:{int(premio / v_min)}]\n")
        for var in varK:
            output_file.write(f"{var.codigo}\n")



if __name__ == '__main__':
    main(sys.argv)



cProfile.run("main(sys.argv)")