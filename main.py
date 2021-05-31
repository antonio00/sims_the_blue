from time import sleep
from casa import Casa
from personagem import Personagem

if(__name__ == "__main__"):
    personagem = Personagem()
    casa = Casa()

    while True:
        print('='*30)
        print(personagem)
        print('='*30)
        opcao = int(input('''
            O que deseja fazer:
            [ 1 ] Acordar Personagem
            [ 2 ] Deixar dormindo
            [ 0 ] Sair
        '''))
        if(opcao == 1):
            while True:
                print('='*30)
                personagem.dormindo = False
                print(personagem)
                print('='*30)
                opcao = int(input('''
            O que deseja fazer:
            [ 1 ] Tomar banho e escovar os dentes
            [ 2 ] Fazer café
            [ 3 ] Pedir café
            [ 4 ] Ir traballhar
            [ 0 ] Sair
        '''))
                if (opcao == 1):
                    personagem.sujo = False
                    print('='*30)
                elif (opcao == 2):
                    if(casa.comida > 0):
                        casa.comida -= 1
                        cafe_da_manha = True
                        personagem.fome = False
                    else:
                        print("Não há comida em casa.")
                elif (opcao == 3):
                    if(personagem.dinheiro >= 20):
                        casa.comida += 2
                        personagem.dinheiro -= 20
                        cafe_da_manha = True
                        personagem.fome = False
                    else:
                        print('Você nao tem dinheiro suficiente')
                elif (opcao == 4):
                    sleep(1)
                    print("-=-=-")
                    print("Você foi trabalhar.")
                    print(personagem)
                    print("-=-=-")
                    recebido = personagem.salario
                    if (personagem.sujo and personagem.fome):
                        print('Você foi trabalhar sujo e com fome')
                        recebido *= 0.1
                    elif (personagem.sujo):
                        print("Como você estava sujo, você levou uma advertência.")
                        recebido *= 0.5
                    elif (personagem.fome):
                        print(
                            "Como você estava com fome, você não rendeu o esperado.")
                        recebido *= 0.3
                    print(
                        f'Você recebeu {recebido:.2f} reais pelo seu trabalho hoje.')
                    personagem.dinheiro += recebido
                    break
                elif (opcao == 0):
                    break
            while True:
                opcao = int(input('''
                O que deseja fazer:
                [ 1 ] Assistir aula Blue
                [ 2 ] Não assistir aula
                [ 3 ] Dormir
                [ 0 ] Sair
            '''))
                if (opcao == 1):
                    print('Você será um ótimo Dev')
                elif (opcao == 2):
                    print('Uma pena ter perdido aula hoje.')
                elif (opcao == 3):
                    personagem.dormindo = True
                    print(personagem)
                    break
                elif (opcao == 0):
                    break
        elif (opcao == 2):
            print('Seu personagem passou dia dormindo')
            recebido = 50
            print(f'Será descontado - R${recebido:.2f} do salario')
        elif (opcao == 0):
            print('Sistema finalizado. Volte sempre')
            break
