import sys

class No:
    def __init__(self, folha=True):
        self.folha = folha
        self.lista_hash = []
        self.lista_nome = []
        self.lista_tamanho = []
        self.filhos = []
    
class ArvoreB:
    def __init__(self, ordem):
        self.raiz = No(folha=True)
        self.ordem = ordem
    
    def inserir(self, hash, nome, tamanho):
        raiz = self.raiz

        if len(raiz.lista_hash) == (2 * self.ordem) - 1:
            nova_raiz = No(folha=False)
            nova_raiz.filhos.append(self.raiz)
            self.div_filhos(nova_raiz, 0)
            self.raiz = nova_raiz
        
        atual = self.raiz
        pilha = []

        while atual:
            i = 0
            while i < len(atual.lista_hash) and hash > atual.lista_hash[i]:
                i += 1
            
            if i < len(atual.lista_nome) and hash == atual.lista_hash[i]:
                return
        
            if atual.folha:
                atual.lista_hash.insert(i, hash)
                atual.lista_nome.insert(i, nome)
                atual.lista_tamanho.insert(i, tamanho)
                break
            else:
                if len(atual.filhos[i].lista_hash) == (2*self.ordem) - 1:
                    self.div_filhos(atual, i)
                    if hash > atual.lista_hash[i]:
                        i += 1
                pilha.append((atual, i))
                atual = atual.filhos[i]
        
        while pilha:
            pai, index_pai = pilha.pop()
            if len(pai.lista_hash) == (2*self.ordem) - 1:
                self.div_filhos(pai, index_pai)
                index_pai += 1
                if hash > pai.lista_hash[index_pai]:
                    index_pai += 1

    def div_filhos(self, pai, index):
        ordem = self.ordem
        filho = pai.filhos[index]

        novo_filho = No(folha=filho.folha)

        pai.lista_hash.insert(index, filho.lista_hash[ordem - 1])
        pai.lista_nome.insert(index, filho.lista_nome[ordem -1])
        pai.lista_tamanho.insert(index, filho.lista_tamanho[ordem - 1])
        pai.filhos.insert(index+1, novo_filho)
        
        novo_filho.lista_hash = filho.lista_hash[ordem:]
        filho.lista_hash = filho.lista_hash[:(ordem - 1)]
        novo_filho.lista_nome = filho.lista_nome[ordem:]
        filho.lista_nome = filho.lista_nome[:(ordem - 1)]
        novo_filho.lista_tamanho = filho.lista_tamanho[ordem:]
        filho.lista_tamanho = filho.lista_tamanho[:(ordem - 1)]

        if not filho.folha:
            novo_filho.filhos = filho.filhos[ordem:]
            filho.filhos = filho.filhos[:ordem]
        
    def pesquisar(self, hash):
        atual = self.raiz

        while atual:
            c = 0
            while c < len(atual.lista_hash) and hash > atual.lista_hash[c]:
                c += 1

            if c < len(atual.lista_hash) and hash == atual.lista_hash[c]:
                cont = 0
                while cont < len(atual.lista_hash):
                    h = atual.lista_hash[cont]
                    n = atual.lista_nome[cont]
                    t = atual.lista_tamanho[cont]
                    output.write(f"{n}:size={t},hash={h}\n")
                    cont += 1
                return True
            elif atual.folha:
                return None
            else:
                atual = atual.filhos[c]
        
        return None

def main(args):
    
    print("Quantidade de argumentos (len(args)): " + str(len(args)))
    for i, arg in enumerate(args):
        print("Argumento " + str(i) + " (args[" + str(i) + "]): " + arg)
    
    input = open(sys.argv[1], "r")
    global output
    output = open(sys.argv[2], "w")

    
    arquivos_input = input.read()
    lista_input = arquivos_input.split("\n")
    ordem = int(lista_input[0])
    poxim = ArvoreB(ordem=ordem-1)

    num_insercoes = int(lista_input[1])
    lista_1 = lista_input[2:]
    cont_in = 0

    while cont_in < num_insercoes:
        entrada = lista_1[cont_in].split(" ")
        nome = str(entrada[0])
        tam = str(entrada[1])
        hash = str(entrada[2])
        poxim.inserir(hash, nome, tam)
        cont_in += 1
    
    lista_2 = lista_1[num_insercoes:]
    num_operacoes = int(lista_2[0])
    cont_op = 1

    while cont_op <= num_operacoes:
        entrada = lista_2[cont_op].split(" ")
        op = str(entrada[0])
        if op == "INSERT":
            nome = str(entrada[1])
            tam = str(entrada[2])
            hash = str(entrada[3])
            poxim.inserir(hash, nome, tam)
            #print("inserido")
            cont_op += 1
        if op == "SELECT":
            hash = entrada[1]
            output.write(f"[{hash}]\n")
            pesquisa = poxim.pesquisar(hash)
            if pesquisa == None:
                output.write("-\n")
            cont_op += 1
    
    input.close()
    output.close()
    

# Executando a funcao main
if __name__ == '__main__':
    # Passando os argumentos do programa
    main(sys.argv)