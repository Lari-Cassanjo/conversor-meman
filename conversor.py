from os import system
system('cls')

pt = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
me = ['A', 'M', 'L', 'P', 'I', 'F', 'J', 'Q', 'E', 'W', 'V', 'R', 'T', 'S', 'U', 'Y', 'X', 'C', 'N', 'B', 'O', 'Z', 'G', 'H', 'D', 'K']

print('---MENU--')
print('\n1- Português para Meman \n2- Meman para Português \n')

while True:
    try:
        selecao = int(input('Escolha a tradução: '))
        if selecao != 1 and selecao != 2:
            raise ValueError
    except ValueError:
        print('Insira um valor válido!')
    else:
        break

print('Digite um número para encerrar o programa.')
if selecao == 1:
    while True: 
        try:
            palavra = input('Digite a palavra que deseja traduzir: ').upper()

            for i in palavra:
                if i in palavra:
                    letrapt = pt.index(i)
                    letrame = me[letrapt]
                    print(letrame,end='')
                else:
                    break
            print('')
        except ValueError:
            print('Fim do Programa')
            break
elif selecao == 2:
    while True: 
        try:
            palavra = input('Digite a palavra que deseja traduzir: ').upper()

            for i in palavra:
                if i in palavra:
                    letrame = me.index(i)
                    letrapt = pt[letrame]
                    print(letrapt,end='')
                else:
                    break
            print('')
        except ValueError:
            print('Fim do Programa')
            break
