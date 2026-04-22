'''
Exercício de Programa 2 - Yahtzee
Thiago Henrique e Frederico Gandini
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

def calcula_pontos_sequencia_baixa(rolados):
    seq_bxa=[[1,2,3,4], [2,3,4,5], [3,4,5,6]]
    c=0
    for lista in range(3):
        c=0
        for num in range(4):
            if seq_bxa[lista][num] in rolados:
                c+=1
            if c == 4:
                return 15  
    return 0

def calcula_pontos_sequencia_alta(rolados):
    seq_alta=[[1,2,3,4,5], [2,3,4,5,6]]
    c=0
    
    for lista in range(2):
        c=0
        for num in range(5):
            if seq_alta[lista][num] in rolados:
                c+=1
            if c == 5:
                return 30  
    return 0

def calcula_pontos_full_house(rolados):
    ret={1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for i in range(len(rolados)):
        ret[rolados[i]]+=1
    dupla = False
    trio = False
    for i in range(len(ret), 0, -1):
        if(ret[i]==3):
            trio=3*i
        elif(ret[i]==2):
            dupla=2*i
    if(dupla and trio):
        return trio+dupla
    else:
        return 0

def calcula_pontos_quadra(rolados):
    ret={1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    c=0
    for i in range(len(rolados)):
        ret[rolados[i]]+=1
    for i in range(len(ret)):
        if ret[i+1] >= 4:
            c=0
            for num in rolados:
                c += num
            return c
    return 0

def calcula_pontos_quina(rolados):
    ret={1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    c=0
    for i in range(len(rolados)):
        ret[rolados[i]]+=1
    for i in range(len(ret)):
        if ret[i+1] >= 5:
            return 50
    return 0

def calcula_pontos_regra_avancada(rolados):
    dic_pontuacao = {
        'cinco_iguais': calcula_pontos_quina(rolados),
        'full_house': calcula_pontos_full_house(rolados),
        'quadra': calcula_pontos_quadra(rolados),
        'sem_combinacao': calcula_pontos_soma(rolados),
        'sequencia_alta': calcula_pontos_sequencia_alta(rolados),
        'sequencia_baixa': calcula_pontos_sequencia_baixa(rolados) 
    }
    return dic_pontuacao

def faz_jogada(rolados, categoria, cartela_de_pontos):
    e_inteiro=False
    try:
        int(categoria)
        e_inteiro=True
    except ValueError:
        e_inteiro=False
    if(e_inteiro):
        simples=calcula_pontos_regra_simples(rolados)
        cartela_de_pontos['regra_simples'][int(categoria)]+=simples[int(categoria)]+1
    else:
        avancada=calcula_pontos_regra_avancada(rolados)
        cartela_de_pontos['regra_avancada'][categoria]+=avancada[categoria]+1
    return cartela_de_pontos