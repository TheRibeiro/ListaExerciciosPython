import random


def criar_baralho(): 
 baralho_Lista = {'as': 1, 'dois': 2, 'tres': 3, 'quatro': 4, 'cinco': 5, 'seis': 6, 'sete': 7, 'oito': 8, 'nove':9, 'dez':10, 'valete':10, 'dama':10, 'rei':10}
 return baralho_Lista

def distribuir_cartas(baralho, numeroCartas):
        quantidadeTirada = 0
        while (numeroCartas < quantidadeTirada):
    
            for i in (baralho,quantidadeTirada):

                carta_tirada = random.choice.pop(baralho)
                quantidadeTirada = quantidadeTirada + 1


baralho = criar_baralho()
numeroCartas = 2
maoDistribuida = distribuir_cartas(baralho, numeroCartas)

print(maoDistribuida)