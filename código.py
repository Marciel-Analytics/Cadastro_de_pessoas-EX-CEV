cont_mais_18 = 0
cont_sexo_M = 0
cont_mulher_20 = 0
while True:
    print('-'*50)
    print('CADASTRE UMA PESSOA')
    print('-' * 50)
    idade = int(input('QUAL A IDADE: '))
    sexo = ' '
    while sexo not in 'FM':
         sexo = str(input('QUAL O SEXO [F/M]: ')).strip().upper()[0]
    print('-' * 50)
    proseguir = ' '
    while proseguir not in 'SN':
        proseguir = str(input('QUER PROSEGUIR [S/N]: ')).strip().upper()[0]

    if idade > 18:
        cont_mais_18 += 1
    if sexo == 'M':
        cont_sexo_M += 1
    if sexo == 'F' and idade <= 20:
        cont_mulher_20 += 1

    if proseguir == 'N':
        break

print('-'*50)
print(f'''
TOTAL DE PESSOAS COM MAIS DE 18 ANOS: {cont_mais_18} 
AO TODO TEMOS {cont_sexo_M} HOMENS CADASTRADOS
E POR FINAL TEMOS {cont_mulher_20} MULHERES COM MENOS DE 20 ANOS''')
print('-'*50)