## O que foi modificado da configuração base original e porquê? ##

Foi dobrada a latência de Miss da Cache L1 e L2 para ter mais impacto no caso do dado não estar na Cache e diminuido pela metade a latência de Hit.
O objetivo disso foi justamente para ter mais impácto se for necessário buscar dados que não estão na cache.

## Quais as três configurações diferentes utilizadas a partir da configuração fixa ##

Variar tamanho da L1 cache de instruções

### Configuração 1: ###

É a mesma que com os valores da configuração fixa

### Configuração 2: ###


### Configuração 3: ###



## Quais algorítmos utilizados? ##

# NÃO FOI ENCONTRADA DIFERENCA NOS RESULTADOS. TENTAR OUTRA ABORDAGEM ALGORÍTIMICA #
Algoritmos iguais, mas sendo compilados modificando a flag de otimização do GCC.
O algorítmo possuí bastantes loops, de forma que podem ser geradas muitas instruções dependendo da otimização.

### Algorítimo 1: ###

**Flag -O2**

Faz com que é otimizado mas somente ativando todas as opções -O2 que não aumentam o tamanho do código gerado.

### Algorítimo 2: ###

**Sem flag**
Não é utilizada nenhuma flag na compilação

### Algorítimo 3: ###

**Flag -03**

O maior nível de otimização possível. Ele permite otimizações que são caras em termos de tempo de compilação e uso de memória.

