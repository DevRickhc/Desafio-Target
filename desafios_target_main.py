import Fibonacci as fib
import InverteString as Is
while True:
    print("""
        Escolha qual Desafio Deseja Ver: 
          [0] - Verifica Numero em Fibonacci
          [1] - Inverter String
          [9] - Sair
""")
    try: 
        escolha = int(input('Sua Escolha: '))
        if escolha == 0:
            fib.desafioFibonacci()
        elif escolha == 1:
            Is.InverteString()
        elif escolha == 9:
            break
        else: 
            print('Opção Invalida!! \nTente Novamente')

    except: 
        print('Opção Invalida!! \nTente Novamente')
