# AED2: Problema do Cavalo

## Participantes
1. Camila Alves
2. Felipe Mitsuo
3. Eraldo Botelho
4. Clarissa Berlim
5. João Coutinho

## Introdução e Descrição do Problema 🐴 
O Problema do Cavalo (ou Knight's Tour) é um problema clássico da matemática e da ciência da computação baseado nas regras do jogo de xadrez. Ele consiste em:

Encontrar uma sequência de movimentos de um cavalo no tabuleiro de xadrez (8x8) de forma que ele visite todas as 64 casas exatamente uma vez, sem repetir nenhuma.

O cavalo, no xadrez, se move em um padrão em “L”: duas casas em uma direção (horizontal ou vertical) e depois uma casa perpendicular. Isso dá até 8 possibilidades de movimento a partir de uma posição, dependendo da borda do tabuleiro.

O desafio é encontrar uma sequência contínua que cubra todo o tabuleiro, o que é chamado de "passeio do cavalo". Quando essa sequência termina na mesma casa de onde começou, o passeio é chamado de fechado; caso contrário, é um passeio aberto.

Este problema é frequentemente usado para estudar:

- Algoritmos de busca e backtracking;
- Aplicações de heurísticas, como a regra de Warnsdorff;
- Conceitos de grafos (representando casas como nós e movimentos como arestas).

## Implementação 💻
O algoritmo desenvolvido tenta construir uma solução recursivamente, explorando possibilidades e voltando atrás (backtrack) quando não há mais movimentos válidos.

A função validos representa a chamada recursiva com tentativa e erro, o que caracteriza backtracking.

A heurística de Warnsdorff é aplicada na função sortPoss, que prioriza as casas com menos opções de movimento subsequente, reduzindo o número de tentativas inúteis e tornando o algoritmo mais eficiente.

- possiveis: retorna todos os movimentos válidos do cavalo a partir da casa atual, respeitando os limites do tabuleiro e evitando repetições.
- sortPoss: aplica a heurística de Warnsdorff, ordenando os próximos movimentos com base na quantidade de saídas possíveis a partir de cada casa.
- validos: realiza o backtracking. Para cada movimento possível, ele testa e continua recursivamente. Se uma sequência válida for encontrada, retorna. Caso contrário, desfaz o último movimento.
- mostrarCaminhoTotal: apenas mostra a trajetória visualmente, não interfere no algoritmo.

## A heurística de Warnsdorff 
É uma estratégia usada para resolver o Problema do Cavalo de forma mais eficiente, reduzindo o número de tentativas que o algoritmo precisa fazer para encontrar uma solução válida.

🧩 O que é essa heurística?

É uma regra prática que ajuda a escolher o próximo movimento do cavalo com maior chance de sucesso, baseada na seguinte ideia:
Sempre mova o cavalo para a casa que possui o menor número de saídas (movimentos válidos futuros).

🧠 Por que isso ajuda?

A lógica por trás é simples:
- Se você vai para uma casa com muitas opções futuras, pode acabar "fechando" o caminho para casas com poucas saídas antes de alcançá-las.
- Se você vai primeiro para casas mais restritas, você evita bloqueios futuros — ou seja, evita ficar "preso" sem movimentos válidos mais à frente.

🔧 Como está implementado no código

A heurística é aplicada na função sortPoss:

    def sortPoss(movimentos, poss):

        numeroDeBifurcacoes = lambda atual: len(possiveis(movimentos + [atual], atual))
    
        newPoss = sorted(poss, key = numeroDeBifurcacoes)
    
        return newPoss

- numeroDeBifurcacoes calcula quantas opções o cavalo teria se fosse para a casa atual.
- A lista de movimentos possíveis é ordenada da casa com menos opções para a casa com mais opções.
- O algoritmo de backtracking testa primeiro as casas com menos saídas, seguindo a heurística.

📈 Resultado

Usando a heurística de Warnsdorff:
- O algoritmo encontra a solução muito mais rápido.
- Evita chamadas desnecessárias.
- Aumenta significativamente a eficiência prática, mesmo que a complexidade teórica ainda seja exponencial.

## Análise da Complexidade 🧮
A complexidade teórica bruta do problema do cavalo, sem heurísticas, é:

O(8⁶⁴) (pior caso), pois em cada uma das 64 casas o cavalo pode fazer até 8 movimentos diferentes.

No entanto, com a heurística de Warnsdorff, o número de caminhos testados é drasticamente reduzido. Em muitos casos, a solução é encontrada em tempo praticamente linear, porque a heurística evita ramificações desnecessárias.

Resumo da complexidade:

Parte do Código | Complexidade Aproximada

possiveis()______ | O(1) (máximo 8 movimentos)

sortPoss()_______ |  O(n × 8) = O(8n)

validos()________ | Exponencial no pior caso, mas próximo de O(n) com a heurística bem aplicada

Como n = 64, o algoritmo com heurística pode terminar em tempo praticamente constante na prática (menos de 1 segundo em muitos computadores), apesar da complexidade teórica ser exponencial.
