frases = ['todos somos programadores','Los hermanos sean unidos porque ésa es la ley primera','¿cómo transmitir a los otros el infinito Aleph?', 'Todos, tu también']

for frase in frases: 
    wordList = frase.split(' ')

    parsedPhrase = []

    for word in wordList:
        accu = ''
        if len(word) > 2:
            if word[-1] == 'o':
                accu = word[:-1] + 'e'
            elif word[-2] == 'o':
                accu = word[:-2] + 'e' + word[-1]
            else: 
                accu = word
        else: 
            accu = word
        parsedPhrase.append(accu)

    frase_t = ' '.join(parsedPhrase)

    print(f'{frase} ---> {frase_t}')
print(f'\'{frases[-1]}\' falla porque tiene una coma y la separación del string en elementos de lista se hace por whitespace, de modo que la primer palabra que se genera es \'Todos,\' donde ni el último ni el ante último caracter son letras \'o\' ')