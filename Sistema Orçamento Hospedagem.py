#Felipe Gomes de Andrade (Engenharia de Software)
#Calculo de Orçamento de Hospedagem (01/10/2024)

import os
from datetime import datetime
os.system("cls")

def leiaInt (msg): #função pra verificar se a variavel está recebendo um número, caso não esteja, vai dar erro e pedir novamente
    while True:
        try:
            valor = int(input(msg))
            return valor
            break
        except ValueError:
            print('')
            print(f'''{vermelho}ERRO! Entrada inválida. Por favor insira um dado válido{reset}''')

def apinvalido (apinv): #função pra validar a entrada do apartamento
    while apinv not in [1, 2]:
        print('')
        print(f'{vermelho}Opção de apartamento inválida!{reset}')
        apinv = leiaInt(f'''Apartamento 
>>''')

    return apinv

def quantdhosp (qntdhosp): #função pra validar a entrada da quantidade de hospedes
    while not (1 <= (qntdhosp) <= 6):
        print('')
        print(f'{vermelho}Quantidade de hóspedes inválida!{reset}')
        qntdhosp = leiaInt(f'''Quantidade de pessoas{ciano} (máx 6){reset} 
>>''')

    return qntdhosp

def periodoinvalido (periodoinv): #função pra validar a entrada do periodo de estadia
    while not (1 <= int(periodoinv) <= 15):
        print('')
        print(f'{vermelho}Período de estadia inválido!{reset}')
        periodoinv = leiaInt(f'''|Perído de estadia{ciano} (máx 15 dias){reset}
>> ''')

    return periodoinv

def verificar_data_de_nascimento(): #função pra validar o formato da data de nascimento
    while True: #looping infinito até receber da forma que eu desejo
        dtnasc = input('|Data de Nascimento (DD/MM/AAAA): ')

        if len(dtnasc) == 10 and dtnasc[2] == '/' and dtnasc [5] == '/':
            return dtnasc
            break #para o looping
        else:
            print('')
            print (f'{vermelho}Formato inválido!! Por favor , use (DD/MM/AAAA).{reset}') #volta pro looping

def calcular_idade(dtnasc): #função para calcular a idade
    nascimento = datetime.strptime(dtnasc, "%d/%m/%Y")
    hoje = datetime.now()
    idade = hoje.year - nascimento.year - ((hoje.month,hoje.day) < (nascimento.month, nascimento.day))

    return idade
           

def verificar_cpf(): #função pra validar o formata do CPF
    while True:
        chave = input('|CPF (000.000.000-XX): ')

        if len(chave) == 14 and chave[3] == '.' and chave[7] == '.' and chave [11] == '-':
            return chave
            break
        else:
            print('')
            print (f'{vermelho}Formato inválido!! Por favor, use (000.000.000-XX).{reset}')
           

def verificar_tel(): #função pra validar o formato do número de telefone
    while True:
        telefone = input('|Telefone (DDD123456789): ')

        if len(telefone) == 11:
            return telefone
            break
        else:
            print('')
            print(f'{vermelho}Formato inválido!! Por favor, use (DDD123456789).{reset}')

#cores
verde = '\033[4;32m'
vermelho = '\033[1;31m'
ciano = '\033[4;36m'
amarelo = '\033[0;33m'
amarelosub = '\033[4;33m'
reset = '\033[0m'

#variaveis
cadastro = 'Cadastro de Usuário'
nome = ''
datanasc = ''
cpf = ''
tel = ''
email = ''
a=''
titorça= 'ORÇAMENTO FINAL DA HOSPEDAGEM'
continuar = ''
hotel = 'HOTEL ANTÔNIO CARLOS'

while continuar != 'n':   #while pra realizar mais de um agendamento no mesmo programa
    os.system('cls')
    print(f'''{reset}{a:*^60}
|{cadastro:^58}|
{a:*^60}''')

#tabela para cadastro do usuário
    print(f'''Dados do usuário 
{a:-^60}
''')

    nome = input('|Nome: ')
    print(f'{a:-^60}')

    #verificando o cpf
    cpf = verificar_cpf()
    print(f'{a:-^60}')

    #verificando a data de nascimento
    datanasc = verificar_data_de_nascimento()
    print(f'{a:-^60}')

    #calculando a idade
    idade = calcular_idade(datanasc)
    if idade < 18:
        print(f'{vermelho}Não é possivel realizar agendamento para menores de idade!{reset}')
        continuar = input('Deseja tentar novamente? [s/n]: ')
        continue

    #verificano o telefone
    tel = verificar_tel()
    print(f'{a:-^60}')
    email = input('|Email: ')
    print('')
    print(f'{a:*^60}')

    #criando o dicionario
    clientes ={
    cpf: [nome, datanasc, tel, email]
    } 

    #adicionando os valores ao dicionário
    clientes[cpf]: [nome, datanasc, tel, email] # type: ignore

    input(f'''{verde}Cadastro Realizado com sucesso{reset}
Pressione {verde}ENTER{reset} para começar o orçamento da sua hospedagem!''')
    
    os.system('cls')

#começa a tabela do agendamento
    print(f'''{a:*^51}
|{hotel:^49}|
{a:*^51}''')
    print(f'''{reset}{a:*^51}         
|               TABELA DE PREÇOS                  |
{a:*^51}
|  Pessoas  |    DIÁRIA AP 1    |    DIÁRIA AP 2  |
{a:*^51}
|     1     |     R$20,00       |     R$25,00     |
|     2     |     R$28,00       |     R$34,00     |
|     3     |     R$35,00       |     R$42,00     |
|     4     |     R$42,00       |     R$50,00     |
|     5     |     R$48,00       |     R$57,00     |
|     6     |     R$53,00       |     R$63,00     |
{a:*^51}''')
    print('')
    ap = leiaInt(f'''|Apartamento
>> ''')
    ap = apinvalido (ap)
    print(f'{a:-^51}')
    pessoas = leiaInt(f'''|Quantidade de pessoas{ciano} (máx 6){reset}
>> ''')
    pessoas = quantdhosp (pessoas)
    print(f'{a:-^51}')

#isso aqui poderia ser substituido por uma lista, mas eu fiz assim e funcionou assim e vai ficar assim porque o programa é meu
#ta calculando o valor, a cada numero que as duas variaveis recebem muda o valor da variavel valor, ta confuso mas certeza que voce entendeu
    valor = 0
    if ap == 1 and pessoas == 1:
        valor = 20
    elif ap ==1 and pessoas ==2:
        valor = 28
    elif ap ==1 and pessoas ==3:
        valor = 35
    elif ap ==1 and pessoas ==4:
        valor = 42
    elif ap ==1 and pessoas ==5:
        valor = 48
    elif ap ==1 and pessoas ==6:
        valor = 53
    elif ap ==2 and pessoas ==1:
        valor = 25
    elif ap ==2 and pessoas ==2:
        valor = 34
    elif ap ==2 and pessoas ==3:
        valor = 42
    elif ap ==2 and pessoas ==4:
        valor = 50
    elif ap ==2 and pessoas ==5:
        valor = 57
    elif ap ==2 and pessoas ==6:
        valor = 63

    dias = leiaInt(f'''|Perído de estadia{ciano} (máx 15 dias){reset}
>> ''')
    dias = periodoinvalido (dias)
    print(f'{a:-^51}')
    pagar = valor * dias
    print(f'{a:*^51}')

#mostrando o orçamento final
    print(f'''{a:=^51}
{titorça:^51}
{a:=^51}
{a:*^51}''')
    print(f'''{amarelosub} 
|Apartamento:{reset} {ap} {amarelosub}
|Quantidade de hóspedes:{reset} {pessoas} {amarelosub}
|Período de estadía:{reset} {dias} {amarelosub}
{a:*^51}
Valor: {verde}R${pagar},00{reset}
{a:*^51}''')
    print('')
    continuar = input(f'Você deseja realizar outro agendamento de hospedagem? {amarelo}[s/n]: ') #sobre poder agendar mais de uma estadia no mesmo programa, aqui está
    while continuar != 's' and continuar != 'n':
        print(f'{vermelho}Apenas são aceitas como resposta {amarelo}"s"{reset} {vermelho}ou{reset}{amarelo} "n"{reset} ')
        print('')
        continuar = input(f'Você deseja realizar outro agendamento de hospedagem? {amarelo}[s/n]:{reset} ')
    
    if continuar == 'n':
        print('')
        print(f'{verde}Obrigado pela preferência!{reset}')
        input('')