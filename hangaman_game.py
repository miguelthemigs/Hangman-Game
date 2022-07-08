import random

arq = open('palavras_forca.txt', 'r')
lista_de_palavras = arq.read().strip().split()
palavra = random.choice(lista_de_palavras).lower()

linhas = len(palavra)*'_'
lista_linha = list(linhas)

print('JOGO DA FORCA'.center(40, ' '))
print('------|\n|\n|\n|\n|\n|\n|\n|______\n')
print(f'Palavra: {linhas}')

erros = 0
tentativas = 1
letras_testadas = []
palavra_string = ' '.join(lista_linha)

while erros < 6: 
    letra = input(f'Tentativa {tentativas}: ')
    if len(letra) > 1:
        print('Insira somente uma letra')
        continue
    tentativas += 1
    if letra in letras_testadas:
            print('Você já testou essa letra')
            continue
    if letra in palavra:
        letras_testadas.append(letra)
        vezes_que_aparece = palavra.count(letra)
        local = palavra.find(letra)
        lista_linha[local] = palavra[local]
        palavra_string = ' '.join(lista_linha)

        if vezes_que_aparece > 1:
            for i in range(1, vezes_que_aparece + 1):
                local = (palavra.find(letra, (local + 1)))
                lista_linha[local] = palavra[local]
        palavra_string = ' '.join(lista_linha)        
        print(palavra_string)
        
        if '_' not in lista_linha:
            print('Você ganhou!')
            break
    else:
        if erros == 0:
            print('------|\n|    ( ) \n|\n|\n|\n|\n|\n|______\n')
        elif erros == 1:
            print('------|\n|    ( ) \n|     |\n|     |\n|\n|\n|\n|______\n')
        elif erros == 2:
            print('------|\n|    ( ) \n|     |\\\n|     |\n|\n|\n|\n|______\n')
        elif erros == 3:
            print('------|\n|    ( ) \n|    /|\\\n|     |\n|\n|\n|\n|______\n')
        elif erros == 4:
            print('------|\n|    ( ) \n|    /|\\\n|     |\n|      b \n|\n|\n|______\n')
        elif erros == 5:
            print('------|\n|    ( ) \n|    /|\\\n|     |\n|    d b \n|\n|\n|______\n')
            print('Você perdeu!')
            print(f'A palavra era {palavra}')
        print(palavra_string)
        letras_testadas.append(letra)
        erros += 1
