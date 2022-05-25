def leiaInt(msg):


    while True:
      try:
        n = int(input(msg))
      except(ValueError,TypeError):
          print('"ERRO": por favor, digite um número inteiro válido!')
          continue
      except(KeyboardInterrupt):
          print('\n\033[31mEntrada de dados interrompida\033[m')
          return 0
      else:
          return n




def ArquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True



def criarArquivo(nome):
   try:
        a = open(nome, 'wt+')
        a.close()
   except:
       print('ERRO na crição do arquivo')
   else:
       print(f'Arquivo {nome} criado com sucesso!')



def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler o arquivo')
    else:
        print('-' * 40)
        print('PESSOAS CADASTRADAS'.center(39))
        print('-' * 40)
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arq, nome = 'desconhecido', idade = 0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
     try:
        a.write(f'{nome}; {idade}\n')
     except:
        print('Houve um erro na hora de escrever os dados')
     else:
         print(f'Novo registro de {nome} adicionado')
         a.close()