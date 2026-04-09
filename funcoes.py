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


