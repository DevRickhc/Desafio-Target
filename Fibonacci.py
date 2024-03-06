def desafioFibonacci():
    seqFibon = []
    while True:
        try :
            #Entrada do numero a ser verificado
            numVerif = float(input('Informe o numero a ser verificado: '))

            #Caso a entrada corra corretamente irá se iniciar a criação de Fibonacci para verificado até o numero ser igual ou menor a Fibonacci
            while  len(seqFibon) < 2 or numVerif > seqFibon[-1] :

                #Considerando que fibonacci iniciasse com 0 e 1 iremos inserir durante o loop
                #seria possivel tambem inserir na inicialização da variavel, porém achei melhor colocar desta forma
                if len(seqFibon) < 2:
                    seqFibon.append(0)
                    seqFibon.append(1)
                else:
                    seqFibon.append(seqFibon[-2] + seqFibon[-1])

            #Após a criação da sequencia é verificado se o numero esta na sequencia de Fibonacci
            if numVerif in seqFibon:
                print(f'O numero {numVerif} esta em fibonacci!!')
            else: 
                print(f'INFELIZMENTE O NUMERO {numVerif} NÃO ESTÁ NA SEQUENCIA DE FIBONACCI !!!')

            #Verifica se o usuario deseja inserir mais numero  ou não
            escolha = input('Deseja Continuar ? [S/N] ').strip().upper()
            if escolha in ('N', 'NAO', 'NÃO'):
                break

        except :
            print('\nNumero informado é Invalido!!!!')



        
        

        
            