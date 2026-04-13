'''
Exercício de Programa 2 - Yahtzee
Thiago Henrique e Frederico Gandini

Número de horas desperdiçadas: 2
'''

# ret = retorno
# seq = sequência
# bxa = baixa
# num = número

# imports
import random as rd 

# função rolar dados
def rolar_dados(n):
    listadados=list()
    for i in range(n):
        listadados.append(rd.randint(1, 6))
    return listadados
    # retorno = lista de dados rolados

# função guardar dado
def guardar_dado(lst_dados_rolados, lst_dados_guardados, i_dado_para_guardar):
    # guarda o dado da lista no index recebido
    dado_a_guardar = lst_dados_rolados[i_dado_para_guardar]
    lst_dados_guardados.append(dado_a_guardar)
    lst_dados_rolados.pop(i_dado_para_guardar)
    lst_dados_rolados_guardados = [lst_dados_rolados, lst_dados_guardados]
    return lst_dados_rolados_guardados
    # retorno = lista de dados guardados

# função de remover dado
def remover_dado(rolados, guardados, i):
    # adiciona o dado sendo removido aos rolados
    rolados.append(guardados[i])
    guardados.pop(i)
    ret=[rolados, guardados]
    return ret
    # retorno = lista de dados [rolados e guardados]

#função pra cálculo dos pontos
def calcula_pontos_regra_simples(rolados):
    ret={1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for i in range(len(rolados)):
        ret[rolados[i]]+=1*rolados[i]
    return ret
    # retorno = pontuação contribuída por cada número

def calcula_pontos_soma(rolados):
    c=0
    for num in rolados:
        c += num
    return c
