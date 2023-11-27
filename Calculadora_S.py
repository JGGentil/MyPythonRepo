import os
def logica_operador():
    while True:
        try:
            global operador
            operador = input('Digite um operador [+] [-] [/] [x] [%]: ')

            if len(operador) > 1:
                print('Digite apenas um operador!')
                continue

            if operador not in '+-/x%':
                print('Digite um operador válido!')
                continue

            if operador in '%':
                break

            numero_1 = input('Digite o primeiro número: ')
            numero_2 = input('Digite o outro número: ')
            numero_1_int = int(numero_1)
            numero_2_int = int(numero_2)

            if int(numero_1) and int(numero_2):
                print('Ok, tudo certo!')

            if operador in '+':
                print(f'{numero_1_int} somado por {numero_2_int} é igual a: {numero_1_int + numero_2_int}')
            elif operador in '-':
                print(f'{numero_1_int} subtraido por {numero_2_int} é igual a: {numero_1_int - numero_2_int}')
            elif operador in '/':
                print(f'{numero_1_int} dividido {numero_2_int} por é igual a: {numero_1_int /  numero_2_int:.0f}')
            elif operador in 'x':
                print(f'{numero_1_int} multiplicado {numero_2_int} é igual a: {numero_1_int *  numero_2_int:.0f}')

            entrada = input('quer "manter" em "%", "voltar" no menu de operadores ou quer "sair"? ')

            if entrada in 'manter' or entrada in 'MANTER' or entrada in 'Manter':
                return calcular_porcentagem()
            elif entrada in 'voltar' or entrada in 'VOLTAR' or entrada in 'Voltar':
                return logica_operador()
            elif entrada in 'sair' or entrada in 'SAIR' or entrada in 'Sair':
                print('programa finalizado!')
                os._exit(0)
            else:
                print('Você não digitou nenhuma das opções disponíveis!')
        except:
            print('O que digitou não foi um número!')
            continue

logica_operador()

def calcular_porcentagem():
    while True:
        global calcular_porcentagem
        numero_3 = input('Digite o número que deseja saber o resultado em porcentagem. Ex: (1000). ')
        porcentagem = input('Agora digite a porcentagem. Ex: (10%). ')
        numero_3_int = int(numero_3)
        porcentagem_int = int(porcentagem)

        if operador in '%':
            resultado = (numero_3_int / 100) * porcentagem_int
            print(f'{porcentagem_int}% de {numero_3_int} resulta em: {resultado:.0f}')

        entrada = input('Quer se "manter" em "%", "voltar" no menu de operadores, ou quer "sair"? ')

        if entrada in 'sair' or entrada in 'SAIR' or entrada in 'Sair':
            print('Programa finalizado!')
            os._exit(0)
        elif entrada in 'manter' or entrada in 'MANTER' or entrada in 'Manter':
            return calcular_porcentagem()
        elif entrada in 'voltar' or entrada in 'VOLTAR' or entrada in 'Voltar':
            return logica_operador()
        else:
            print('Você não digitou nenhuma das opções disponíveis!')

calcular_porcentagem()
