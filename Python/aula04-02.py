def menu_simples():
    opcao = ""

    while opcao != "3":
        print(" 1 - Ver mensagens ")
        print(" 2 - Repetir Menu ")
        print(" 3 - Sair ")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("Você escolheu ver a primeira mensagem")
        elif opcao == "2":
            print("Você escolheu ver a segunda mensagem")
        elif opcao != "3":
            print("Opção inválida")
    print("Programa encerrado.")

menu_simples()