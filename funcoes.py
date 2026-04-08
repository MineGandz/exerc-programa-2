'''
Exercício de Programa 2 - Yahtzee
Thiago Henrique e Frederico Gandini

Número de horas desperdiçadas: 0.5
'''

# imports
import random as rd 

# função rolar dados
def rolar_dados(n):
    listadados=list()
    for i in range(n):
        listadados.append(rd.randint(1, 6))
    return listadados

# função guardar dado
def guardar_dado(lst_dados_rolados, lst_dados_guardados, i_dado_para_guardar):
    dado_a_guardar = lst_dados_rolados[i_dado_para_guardar]
    lst_dados_guardados.append(dado_a_guardar)
    lst_dados_rolados.pop(i_dado_para_guardar)
    lst_dados_rolados_guardados = [lst_dados_rolados, lst_dados_guardados]
    return lst_dados_rolados_guardados

