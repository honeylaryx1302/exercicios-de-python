import os

restaurantes = ['pizza','xp']

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
           
     
opcao_escolhida = int(input('escolha uma opção'))
#print('você escolheu a opção', opção_escolhida)
#print(f' vocêescolheu a opção {opção_escolhida}')

def exibir_subtitulo(texto):
    os.system('clear')
    print(texto)
    print()

def escolher_opcao():
 
    if opcao_escolhida == 1:
            print('cadastrar restaurante')
    elif opcao_escolhida == 2:
            print('listar restaurantes')
    elif opcao_escolhida == 3:
            print('ativar restaurantes')
    else:
        finalizar_app()

def main():
   os.sistem('clear')
   exibir_nome_do_programa()
   exibir_opcoes()
   escolher_opcao()

   if __name__ == '__main__':
       main()