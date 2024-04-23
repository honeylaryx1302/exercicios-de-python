import os

restaurantes = [{'nome':'restaurante XP','categoria':'alimento','ativo':False},
                {'nome':'santa','categoria':'carne','ativo':True},
                {'nome':'CWB','categoria':'sushi','ativo':False}]

def exibir_nome_do_programa():
 print ("""sabor express
""")
def exibir_opcoes():
 print('1. cadastrar restaurante')
 print('2. listar resturante ')
 print('3. ativar restaurante')
 print('4. sair')

def finalizar_app():
    exibir_subtitulo('finalizar app')

def voltar_ao_menu_principal():
   input('\n Digite uma tecla "enter"para voltar ao menu principal')
   main()    

def opcao_invalida():
    print('opcao invalida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
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
    exibir_subtitulo('listando os restarantes')

    print(f'{"nome do restaurante".ljust(22)} | {"categoria".ljust(20)} | status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
   exibir_subtitulo('alternado estado do restaurante')
   nome_restaurante = input('digite o nome do retaurante que deseja alterar o estado:')
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
   os.system('clear')
   exibir_nome_do_programa()
   exibir_opcoes()
   escolher_opcao()

if __name__ == '__main__':
    main()