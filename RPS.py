from random import randint



print('Rock, Paper, Scissor!')
user_escolha = ''
user_escolha = input('Escolha Pedra, Papel ou Tesoura:\n')
user_escolha = user_escolha.lower()


#1 = rock/pedra
#2 = paper/papel
#3 = scissor/tesoura

##cpu escolhe valor entre 1-3
valor = int(0)
valor = randint(1, 3)
cpu = ''
if (valor == 1):
    cpu = 'Pedra'
if (valor == 2):
    cpu = 'Papel'
if(valor == 3):
    cpu = 'Tesoura'

print('o CPU escolheu: ' + cpu)



##3 opções
if (valor == 1 and user_escolha == 'papel'):
    print('Você perdeu!')

elif (valor == 1 and user_escolha == 'tesoura'):
    print('Você perdeu!')

elif (valor == 1 and user_escolha == 'pedra'):
    print('Empate!')

##3 opções
elif (valor == 3 and user_escolha == 'pedra'):
    print('Você ganhou!')

elif (valor == 3 and user_escolha == 'tesoura'):
    print('Empate!')

elif (valor == 3 and user_escolha == 'papel'):
    print('Você perdeu!')

## 3 opções
elif (valor == 2 and user_escolha == 'papel'):
    print('Empate!')

elif (valor == 2 and user_escolha == 'tesoura'):
    print('Você ganhou!')

elif (valor == 2 and user_escolha == 'pedra'):
    print('Você perdeu!')