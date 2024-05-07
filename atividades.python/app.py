import os

restaurantes = [{'nome':'restaurante XP','categoria':'alimento','ativo':False},
                {'nome':'santa','categoria':'carne','ativo':True},
                {'nome':'CWB','categoria':'sushi','ativo':False}]

def exibir_nome_do_programa():
 '''esta função é responsavel por exibir o nome do programa
 output:
 -exibe o nome do programa
 '''

print ("""sabor express
""")
def exibir_opcoes():
 '''esta função é rsponsavel por exibir as opções
    output:
    -nos motra as opções como cadastrar,listar,ativar ou sair do restaurante
  '''

 print('1. cadastrar restaurante')
 print('2. listar resturante ')
 print('3. ativar restaurante')
 print('4. sair')

def finalizar_app():
    '''Esta opção é responsavel por finalizar o aplicativo
    output:
    -sai do restaurante
     '''

    exibir_subtitulo('finalizar app')

def voltar_ao_menu_principal():
    '''Essa funcao é reponsavel por voltar ao menu pricipal assim que voce aperta o enter
    
    output:
    -retorna a tela inicial do aplicativo
    '''

    input('\n Digite uma tecla "enter"para voltar ao menu principal')
    main()    

def opcao_invalida():
    '''esta funcao e responsavel por nos mostrar se a opcao é invalida
    
    output:
    -retorna ao menu principal caso a opcao seja invalida
    '''

    print('opcao invalida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''Esta funcao é responsavel por exibir o subtitulo
    
    output:
    -organiza os textos e as linhas,organiza as categorias nas linhas
    '''

    os.system('clear')
    linha = '*' * (len)(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_resturante():
   '''Essa função é responsavel por cadastrar um novo restaurante
 inputs:
   -nome do restaurantes
   -categoria
   
   output:
   -Adiciona um novo restaurante à lista de restaurantes
   '''

   exibir_subtitulo('cadastro de novos restaurantes:')
   nome_do_restaurante = input('digite o nome do novo restaurante')
   categoria = input (f'digite a categoria do resturante {nome_do_restaurante}: ')
   dado_do_restaurante ={'nome':nome_do_restaurante,'categoria':categoria,'ativo':False}
   restaurantes.append(dado_do_restaurante)
   print(f'o restaurante{nome_do_restaurante} foi cadastrado com sucesso!')
   voltar_ao_menu_principal()

def listar_restaurante():
    '''esta funcao é responsavel por lostar o restaurante
    
    output:
    -mostra o nome do restaurante,as categorias e os status do restaurante
    '''

    exibir_subtitulo('listando os restarantes')

    print(f'{"nome do restaurante".ljust(22)} | {"categoria".ljust(20)} | status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
   '''esta funcao é responsavel por alternaar o estado do restaurante
     input:nome do restaurante
    
   output:
    -fazer alternacao do estado do restaurante
   '''

   exibir_subtitulo('alternado estado do restaurante')
   nome_restaurante = input('digite o nome do restaurante que deseja alterar o estado:')
   restaurante_encontrado = False

   for restaurante in restaurantes:
    if nome_restaurante == restaurante['nome']:
        restaurante_encontrado = True
        restaurante['ativo'] = not restaurante['nome']
        mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso'if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
        print(mensagem)

   if not restaurante_encontrado:
     print('O o restaurante nao foi encontrado')
   voltar_ao_menu_principal()

def escolher_opcao():
    '''esta funcao é responsavel por escolher as opcoes 
    
    output:
    -escolha das opcoes
    '''
try:
    opcao_escolhida = int(input('escolha uma opcao:'))
    
    if opcao_escolhida == 1:
           cadastrar_novo_resturante()
    elif opcao_escolhida == 2:
           listar_restaurante()
    elif opcao_escolhida == 3:
            alternar_estado_restaurante()
    elif opcao_escolhida == 4:
            finalizar_app()
    else:
      opcao_invalida()

except:
    opcao_invalida()

def main():
    '''esta funcao é responsavel por garantir que as funcoes sejam executadas quando o programa for iniciado
    
    output:
    -faz com que as funcoes sejam executadas corretamente assim que o programa for iniciado
    '''

    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()