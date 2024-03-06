def InverteString():

    while True:
        #Entrada da String
        stringInverte = input('informe a String: ').strip()

        #loop que irá retornar a string Invertida
        for n in stringInverte:
            if n == stringInverte[0]:
                stringInvertida = ''
                stringInvertida = n + stringInvertida
            else :
                stringInvertida = n + stringInvertida
        stringInverte = stringInvertida
        stringInvertida = ''
        print(stringInverte)
        escolha = input('Deseja inserir nova palavra? [S/N] ').strip().upper()
        if escolha in ('N', 'NAO', 'NÃO'):
            break

