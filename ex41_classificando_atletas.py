from datetime import date
atual = date.today().year

nasc = int(input('Qual o seu ano de nascimento? '))
idade = atual - nasc
if idade <= 9:
    print(f'Com {idade} anos sua categoria é MIRIM. ')
elif idade <= 14: 
    print(f'Com {idade} anos sua categoria é INFANTIL.')
elif idade <= 19 : 
    print(f'Com {idade} anos sua categoria é JÚNIOR.')
elif idade <= 25: 
    print(f'Com {idade} anos sua categoria é SÊNIOR.')
else: 
    print(f'Com {idade} anos sua categoria é MASTER.')

