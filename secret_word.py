"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

while True:

    
    palavra_secreta = 'amor'
    letra_acertada = ''
    tentativa = 0
    
    # Start
    print('BEM VINDO AO ADIVINHE A PALAVRA\n')
    comeco = input(
        '\n Vamos começar ? \n [s]im \n [n]ão para sair\n').lower().startswith('s')

    if comeco:

        while True:
            # Solicita a letra
            letra_informada = input('Informe a Letra desejada : ').lower()
            tentativa += 1

            # Checa se foi apenas uma letra informada
            if len(letra_informada) > 1:
                print('\nApenas uma letra por vez.')
                continue
            
            # Salvo as letras acertadas
            if letra_informada in palavra_secreta:
                letra_acertada += letra_informada


            resposta = ''

            for letra in palavra_secreta:  # verifico letra por letra na palavra_secreta
                if letra in letra_acertada:  # verifico se a letra está nas letras acertadas
                    resposta += letra  # exibo a letra se ele for acertada
                else:
                    resposta += '*'  # exibo * se for errada

            print(f'A palavra até o momento é : {resposta}')

            if resposta == palavra_secreta:
                os.system('cls')
                print('Parabéns você Acertou!')
                print(f'A palavra era {resposta}')
                print(f'Tentativas {tentativa}')
                letra_acertada = ''
                tentativa = 0
                break
    else:
        break
