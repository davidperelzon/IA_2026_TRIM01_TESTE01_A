# ==============================================================================
# Questão 1: Manipulação de Dicionário (20 pontos)
# ==============================================================================
# Dado um texto (string), retorne um dicionário onde as chaves são as palavras 
# e os valores são o número de vezes que cada palavra aparece no texto.
dicionario = {}
def contar_palavras(texto):
    palavras = texto.split()
    for palavra in palavras:
        if palavra in dicionario:
            dicionario[palavra] += 1
        else:
            dicionario[palavra] = 1
    return dicionario

print(contar_palavras("ola eu sou o salustiano e eu sou o cara mais brabo do mundo inteiro principalmente quando se trata de python"))