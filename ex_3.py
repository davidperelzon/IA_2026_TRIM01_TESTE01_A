# ==============================================================================
# Questão 3: Funções Lambda e Filter (20 pontos)
# ==============================================================================
# Dada uma lista de nomes, utilize a função `filter` e uma função `lambda` 
# para retornar uma lista apenas com os nomes que possuem 3 letras ou menos.
def filtrar_nomes_curtos(nomes):
    return list(filter(lambda nome: len(nome) <= 3, nomes))
print(filtrar_nomes_curtos(["Ana", "João", "Lia", "Juca", "Leo"]))