from funcoes import *
cartela_de_pontos = {
    'regra_simples':  {
        1:-1,
        2:-1,
        3:-1,
        4:-1,
        5:-1,
        6:-1
    },
    'regra_avancada' : {
        'sem_combinacao':-1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}
imprime_cartela(cartela_de_pontos)
#juntar lista guardados e rolados
output=[]
notinvalida=1
for i in range(12):    
    rolados=[]
    rolados=rolar_dados(5)
    guardados=[]
    print("Dados rolados:", rolados)
    print('Dados guardados:', guardados)
    rerrolagens=0
    while True:  
        
        if(notinvalida>0):
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        notinvalida=1
        resposta=input()
        try:
            resposta=int(resposta)
        except ValueError:
            print("Opção inválida. Tente novamente.")
            notinvalida=0
            continue
        if(resposta==1):
            print('Digite o índice do dado a ser guardado (0 a 4):')
            index=int(input())
            guardados=guardar_dado(rolados, guardados, index)[1]
            notinvalida=1
        elif(resposta==2):
            print("Digite o índice do dado a ser removido (0 a 4):")
            index=int(input())
            guardados=remover_dado(rolados, guardados, index)
            notinvalida=1
        elif(resposta==3):
            if(rerrolagens<2):
                rolados=rolar_dados(len(rolados))
                rerrolagens+=1
            else:
                print("Você já usou todas as rerrolagens.")
            notinvalida=1
        elif(resposta==4):
            imprime_cartela(cartela_de_pontos)
            notinvalida=1
        elif(resposta==0):
            print("Digite a combinação desejada:")
            output=rolados+guardados
            while True:
                
                categoria=input()
                try:
                    int(categoria)
                    e_inteiro=True
                except ValueError:
                    e_inteiro=False
                if(e_inteiro):
                    if(int(categoria) not in cartela_de_pontos['regra_simples']):
                        print("Combinação inválida. Tente novamente.")
                    elif(cartela_de_pontos['regra_simples'][int(categoria)] == -1):
                        faz_jogada(output, categoria, cartela_de_pontos)
                        notinvalida=1
                        break
                        
                    else:
                        print("Essa combinação já foi utilizada.")
                else:
                    if (categoria not in cartela_de_pontos['regra_avancada']):
                        print("Combinação inválida. Tente novamente.")
                    elif(cartela_de_pontos['regra_avancada'][categoria]<0):
                        faz_jogada(output, categoria, cartela_de_pontos)
                        notinvalida=1
                        break
                    
                    else: 
                        print("Essa combinação já foi utilizada.")
                notinvalida=1
                        
        else:
            print("Opção inválida. Tente novamente.")
            notinvalida=0
            continue
        if(resposta==0):
            break
        else:
            print("Dados rolados:", rolados)
            print('Dados guardados:', guardados)
soma1=0
soma2=0
total=0
for i in cartela_de_pontos['regra_simples']:
    if(cartela_de_pontos['regra_simples'][i]>=0):
        soma1+=cartela_de_pontos['regra_simples'][i]
    else:
        cartela_de_pontos['regra_simples'][i]=0
for i in cartela_de_pontos['regra_avancada']:    
    if(cartela_de_pontos['regra_avancada'][i]>=0):
        soma2+=cartela_de_pontos['regra_avancada'][i]
    else:
        cartela_de_pontos['regra_avancada'][i]=0
imprime_cartela(cartela_de_pontos)
if(soma1>=63):
    soma1+=35
total+=soma1+soma2
print("Pontuação total:", total, sep=" ")
