# TRABALHO PRÁTICO 03  

# IMPLEMENTAÇÃO E ANÁLISE DE ALGORITMOS DE CAMÍNHO MÍNIMO 

 

## Introdução: 
 
Foi proposto um trabalho prático para matéria de Otimização I. Nesse trabalho seria necessario implementar 3 algoritmos de análise de caminho mínimo: 

 

*Algoritmo de Dijkstra*

*Algoritmo de Bellman-Ford*  

*Algoritmo de Floyd-Warshall* 

 

Esses três algoritmos deveriam ser implementados e analisados de maneira comparativa para grafos gerados aleatoriamente. 

 

 

## Implementação: 

Primeiramente foram geradas 3 funções para geração de grafos: 
 
*GerarGrafoPositivo* 

*GerarGrafoNegativo* 

*GerarGrafoDenso*

A função mais simples entre essas três é a *“GerarGrafoDenso”*, ela gera um grafo completamente conectado onde todas as arestas estão diretamente conectadas. A função *“GerarGrafoPositivo”* é uma versão dessa mesma função com a possibilidade aleatória de gerar caminhos de distância infinita no meio do grafo.  

A parte mais complexa foi a função *"GerarGrafoNegativo”*. A interação do Bellman-Ford com ciclos negativos e a geração aleatória criou vários problemas. A maneira mais simples de resolver isso foi gerar um grafo pequeno para a análise com números negativos. Ainda são gerados alguns grafos com ciclos negativos dando erro no processo, mas após rodar algumas vezes é retornado um grafo sem esses caminhos possibilitando a análise do problema.

Após isso, os 3 códigos principais dos algoritmos de caminhos mínimos foram implementados sem nenhum grande problema. As funções de Dijkstra e de Bellman-Ford retornam, cada uma, a lista do caminho mínimo para cada outra aresta que não seja a passada pra a função como parâmetro. Já a função de Floyd-Warshall retorna uma matriz otimizada das distancias entre as arestas. 

Por fim é printado todos os tempos do código para análise utilizando a biblioteca TimeIT pois apenas a biblioteca time do python não estava conseguindo retornar o tempo de execução das funções que ocorrem de maneira mais rápida. 

 

## Análise: 

Análise com grafos de poucas arestas temos: 

Grafo Positivo: 7 nos 

Grafo Negativo: 7 nos 

Grafo Denso: 7 nos 

 

![Grafo Pequeno](imagens\GrafoPequeno.jpeg)

 

Em termos de eficiência, Dijkstra executou na metade do tempo do Bellman em gráficos pequenos com valores positivos. Já o algoritmo de Floyd foi ainda mais rápido que o Dijkstra, multiplicado pelo número de nós no grafo. 

  

Quando se trata de grafos com distâncias negativas, a análise se concentra no algoritmo de Bellman, que é capaz de lidar com essa situação. Nesse caso, o Bellman foi mais rápido que o Floyd, porém mais lento considerando que seria executado uma vez para cada aresta do grafo. 

  

Por fim, em grafos densos, o algoritmo de Bellman levou mais tempo para calcular um único nó em comparação ao Floyd, que retornou a matriz completa mais rapidamente. 

 

Análise com grafos de poucas arestas (excluindo o com números negativos) temos: 

Grafo Positivo: 150 nos 

Grafo Denso:   150 nos 

 
![Grafo Grande](imagens\GrafoGrande.jpeg)


No caso de um grafo com valores positivos, a análise anterior se mantém, com a diferença de que a eficiência do Dijkstra se aproximou da do Floyd, considerando que o Dijkstra executou um número de vezes igual ao número de arestas no grafo. 

Além disso, em um grafo denso, com muitas arestas, o algoritmo de Dijkstra se mostrou significativamente superior aos outros métodos analisados. 