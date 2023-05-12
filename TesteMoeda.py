import moeda

p = float(input('Digite o preço em reais'))
print(f'metade de {p} é {moeda.metade(p)}')

taxa = int(input('Qual a taxa de compra desse produto?'))

print(f'Com a taxa de {int (taxa / 10)}% O aumento no Produto ficou de {moeda.aumentar(p, taxa)}')