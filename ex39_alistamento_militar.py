from datetime import date
nasc = int(input('Que ano você nasceu? '))
ano = date.today().year 
idade = (ano - nasc)
idade2 = 18 - idade
idade3 =idade - 18
if idade < 18:
    print(f'Você tem {idade} anos, ainda não pode se alistar.')
    if idade == 17:
        print(f'Falta {idade2} ano para vc se alistar.')
    elif idade < 17: 
        print(f'Faltam {idade2} anos para vc se alistar.')
    print(f'Seu alistamento será em {ano + idade2}')
elif idade == 18:
    print(f'Você tem {idade} anos, já está na hora de se alistar.')
elif idade > 18:
    print(f'Você passou {idade3} anos, sua situação está irregular.') 
    print(f'Seu alistamento era em {ano - idade3}')       