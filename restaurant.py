def entradas(lista,total):
    while True:
        print("Entradas:")
        print("1. Camarão frito Info: Camarão empadado e frito em oleo(10.00€)")
        print("2. Pão de alho I Info: Pão de alho com manteiga (5.00€)")
        print("3. Pâo de alho com queijo Info: Pão de alho com queijo (7.00€)")
        print("4. Salada de tomate Info: Salada com tomates e pepino (6.00€)")
        print("5. Salada de alface Info: Salada com alface e tomates (5.00€)")
        print("6. Voltar ao menu principal")
        choice = input("Por favor, selecione uma entrada: ")
        choice = choice.split()
        if choice == '1' or (choice[0].casefold() == 'Camarão' or choice[0].casefold() == 'Camarao') and choice[1].casefold() == 'frito':
            print("Você selecionou Camarão frito.")
            quality = input("Quantos camarões fritos você gostaria de pedir? ")
            if quality.isdigit():                 quality = int(quality)
            list.append("Camarão frito"+str(quality)+"unidades")
            total = 10.00*quality
        elif choice == '2' or (choice[0].casefold() == 'Pão' or choice[0].casefold() == 'Pao') and choice[1].casefold() == 'de' and choice[2].casefold() == 'alho' :
            print("Você selecionou Pão de alho.")
            if quality.isdigit():                 quality = int(quality)
            list.append("Pão de alho"+str(quality)+"unidades")
            total += (5.00*quality)
        elif choice == '3' or (choice[0].casefold() == 'Pão' or choice[0].casefold() == 'Pao') and choice[1].casefold() == 'de' and choice[2].casefold() == 'alho' and choice[3].casefold() == 'com' and choice[4].casefold() == 'queijo':
            print("Você selecionou Pão de alho com queijo.")
            if quality.isdigit():                 quality = int(quality)
            list.append("Pão de alho com queijo"+str(quality)+"unidades")
            total += (7.00*quality)
        elif choice == '4' or (choice[0].casefold() == 'Salada' and choice[1].casefold() == 'de' and choice[2].casefold() == 'tomate'):
            print("Você selecionou Salada de tomate.")
            if quality.isdigit():                 quality = int(quality)
            list.append("Salada de tomate"+str(quality)+"unidades")
            total += (6.00*quality)
        elif choice == '5' or (choice[0].casefold() == 'Salada' and choice[1].casefold() == 'de' and choice[2].casefold() == 'alface'):
            print("Você selecionou Salada de alface.")
            if quality.isdigit():                 quality = int(quality)
            list.append("Salada de alface"+str(quality)+"unidades")
            total += (5.00*quality)
        elif choice == '6' or (choice[0].casefold() == 'Voltar' and choice[1].casefold() == 'ao' and choice[2].casefold() == 'menu' and choice[3].casefold() == 'principal'):
            print("Voltando ao menu principal.")
            break
        else:
            print("Seleção inválida. Por favor, tente novamente.")
    return total

def menu():
    list = []
    total = 0
    while True:
        print("Bem vindo ao Restaurant!")
        print("1. Entradas")
        print("2. Sopas")
        print("3. Carne")
        print("4. Peixe")
        print("5. Sobremesas")
        print("7. Acabar o pedido")
        choice = input("Por favor, selecione uma categoria (1-7): ")
        choice = choice.split()
        if choice == '1' or (choice[0].casefold() == 'Entradas'.casefold()):
            print("Você selecionou Entradas.")
            total = entradas(list,total)
        elif choice == '2'or (choice[0].casefold() == 'Sopas'.casefold()):
            print("Você selecionou Sopas.")
        elif choice == '3' or (choice[0].casefold() == 'Carne'.casefold()):
            print("Você selecionou Carne.")
        elif choice == '4' or (choice[0].casefold() == 'Peixe'.casefold()):
            print("Você selecionou Peixe.")
        elif choice == '5' or (choice[0].casefold() == 'Sobremesas'.casefold()):
            print("Você selecionou Sobremesas.")
        elif choice == '7' or (choice[0].casefold() == 'Acabar' and choice[1].casefold() == 'o' and choice[2].casefold() == 'pedido'):
            print("Obrigado pelo seu pedido!")
            break
        else:
            print("Seleção inválida. Por favor, tente novamente.")

if __name__ == "__main__":    
    menu()
    