# ==============================================================================
# Questão 2: Funções Lambda e Map (20 pontos)
# ==============================================================================
# Dada uma lista de números inteiros, utilize a função `map` em conjunto com 
# uma função `lambda` para criar e retornar uma nova lista onde cada elemento 
# é o quadrado do valor original.
def elevar_ao_quadrado(numeros):
    return list(map(lambda x: x**2, numeros))
print(elevar_ao_quadrado([1, 2, 3, 4,]))