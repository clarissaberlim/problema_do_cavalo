from os import system as sys
import time

def possiveis(movimentos, casaAtual):
    possiveis = []
    for i in range(-2, 3):
        for j in range(-2, 3):
            casa = casaAtual+j+8*i
            if i*j != 0 and i != j and 0 <= casa//8 < 8 and 0 <= casaAtual%8+j < 8 and i+j != 0 and casa not in movimentos:
                possiveis.append(casa)
    return possiveis

def sortPoss(movimentos, poss):
    numeroDeBifurcacoes = lambda atual: len(possiveis(movimentos + [atual], atual))
    newPoss = sorted(poss, key = numeroDeBifurcacoes)
    return newPoss

def validos(movimentos, casaAtual):
    if len(movimentos) == 64:
        return movimentos
    poss = sortPoss(movimentos, possiveis(movimentos, casaAtual))
    if len(poss) != 0:
        for i in poss:
            movimentos += [i]
            caminho = validos(movimentos, i)
            if caminho:
                return caminho
            movimentos.pop()
    else:
        return None

def mostrarCaminhoParcial(movimentos, limite):
    print(" "*3, end="")
    for i in range(8):
        print(f"{chr(97+i):^3}", end="")
    print("")
    for i in range(8):
        print(f"{i+1:^3}", end="")
        for j in range(8):
            print(f"{movimentos[i*8+j] if movimentos[i*8+j] <= limite else ' ':3}", end="")
        print("")
    print("")

def mostrarCaminhoTotal(movimentos):
    for i in range(64):
        sys("cls")
        mostrarCaminhoParcial(movimentos, i+1)
        time.sleep(0.15)

def main():
    movimentos = validos([0], 0)
    movimentos = {i:movimentos.index(i)+1 for i in movimentos}
    mostrarCaminhoTotal(movimentos)
    fim = input("Digite a tecla ENTER para sair.")

if __name__ == "__main__":
    main()
