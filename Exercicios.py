
##Criação de função

def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg} x {comp} é de {a} m2')
    


#Programa Principal
print( 'Controle de terrenos')
print('$'* 30)    
 
#Criação de variaveis

l = float(input('Largura'))
c = float(input('Comprimento'))          
    
área(l, c)
print(área)