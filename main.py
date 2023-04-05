from time import sleep
print('Olá, seja bem-vindo.')
rs = float(input('Qual o valor que você tem na sua carteira em R$?'))
print('CARREGANDO...')
sleep(2)
us = 5.03
final = rs / us
print('Com {:.2f} R$ podera comprar {:.2f} $'.format(rs , final))
