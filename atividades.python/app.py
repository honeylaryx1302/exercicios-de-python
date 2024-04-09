import os

print ("""sabor express
       """)

print('1. cadastrar restaurante')
print('2. listar resturante ')
print('3. ativar restaurante')
print('4. sair')

opcao_escolhida = int(input('escolha uma opção'))
#print('você escolheu a opção', opção_escolhida)
#print(f' vocêescolheu a opção {opção_escolhida}')

def finalizar_app():
    os.system('cls')
    print('encerrando o programa \n')

    if opcao_escolhida == 1:
        print('cadastrar restaurante')
    elif opcao_escolhida == 2:
        print('listar restaurantes')
    elif opcao_escolhida == 3:
        print('ativar restaurantes')
    else:
        finalizar_app()