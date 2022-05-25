from time import sleep
from uteis import *

arq = 'Dados.txt'

if not ArquivoExiste(arq):
    criarArquivo(arq)

while True:
    print('='*40)
    print('MENU PRINCIPAL'.center(39))
    print('='*40)
    print('''
\033[1;36m1- Ver pessoas cadastradas
    
2- Cadastrar novas pessoas
    
3- Sair do Sistema\033[m
          ''')
    print('~'*40)


    try:
     option = int(input('SUA OPÇÃO: '))

     if option == 1:
         lerArquivo(arq)
         sleep(1)





     if option == 2:
         print('-'*40)
         print('NOVO CADASTRO'.center(39))
         print('-'*40)
         pessoas = str(input('NOME: ')).upper()
         idade = leiaInt('IDADE: ')
         cadastrar(arq, pessoas, idade)
         sleep(1)



     if option == 3:
         print('-' * 40)
         print('SAINDO DO SISTEMA'.center(39))
         print('-' * 40)
         break



     if option > 3 or option < 1:
         print('\033[1;31mERRO! Atenção, valor inválido!\033[m')
     sleep(1)


    except(TypeError, ValueError):
     print('\033[1;31mERRO! Atenção, valor inválido!\033[m')
     sleep(1)

print('FINALIZANDO O PROGRAMA...')
sleep(1)
print('ATÉ LOGO!')








