nota1 = float(input('Diite sua primeira nota:'))
nota2 = float(input('Diite sua segunda nota:'))
media = (nota1 + nota2) / 2
if media < 5:
    print(f'Sua media foi {media} você foi REPROVADO.')
elif 7 > media >= 5 :  
    print(f'Sua media foi {media} você está de RECUPERÇÃO.')    
if media >=7:
    print(f'Sua media foi {media} você foi APROVADO.')
    print('PARABÉNS!!!!')



