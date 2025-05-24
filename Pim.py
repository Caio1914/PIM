while True:
    #Etapa 1: Boas-vindas
    print("-----------------------------------------------------------------------------------------------------------------")
    print("-----------------------------------------------------------------------------------------------------------------")
    print("--- BEM VINDO(A) ---")
    nome = input("\nOlá! Por favor, digite seu nome: ")
    idade = input("Por favor, digite sua idade: ")
    print(f"\nSeja bem-vindo(a), {nome}! Você tem {idade} anos.")
   
#Na etapa 1 vai mostrar na tela as boas vindas e ira pedir para digitar seu nome e sua idade

    #Etapa 2: Consentimento
   
    print("\n--- CONSENTIMENTO ---")
    consentimento = input("\nVocê autoriza o uso de seus dados para análises estatísticas? (sim/não): ").strip().lower()

    if consentimento != 'sim':
        print("Você não consentiu com o uso dos dados. Retornando ao inicio")
        continue
    else:
        print("ótimo, você consentiu")
   
#Na etapa 2 vai pedir seu consentimento, se sim vai continuar a etapa se não retorna para etapa 1
        
    #Etapa 3: Sobre a Tecnologia da Informação

    print("\n--- SOBRE A TECNOLOGIA DA INFORMÇÃO ---")
    print("\nTecnologia da Informação (TI) é o conjunto de todas as atividades e soluções providas por recursos de computação para armazenamento, ")
    print("processamento, proteção e transmissão de informações. É fundamental para empresas, governos e para a vida moderna de modo geral.")
    
    input("\nDigite ou clique ENTER para continuar para a próxima etapa...")
   
#Na etapa 3 vai falar brevemente sobre a Tecnologia da Informação e para continuar digite ou aperte ENTER

    #Etapa 4: Representação de Algoritmos
    while True:
       
        print("\n--- REPRESENTÇÃO DE ALGORITMOS ---")
        print("\nEscolha uma das opções abaixo:")
        print("1 - Pseudocódigo")
        print("2 - Fluxograma")
        escolha = input("Digite 1 ou 2: ").strip()
       

        if escolha == "1":
            print("\nPseudocódigo é uma forma textual de descrever algoritmos, usando uma linguagem parecida com a natural, facilitando o entendimento lógico.")
           
        elif escolha == "2":
            print("\nFluxograma é uma representação gráfica dos passos de um algoritmo, usando símbolos como setas, retângulos e losangos.")
           
        else:
            print("\nOpção inválida. Tente novamente.")
            
            continue

        comando = input("Digite 'continuar' para seguir ou 'voltar' para escolher outra opção: ").strip().lower()
        if comando == "continuar":
            break
        
#Na etapa 4 vai mostrar duas opções de Representação de Algoritmos, 1 Pseudocódigo/ 2 Fluxograma, o ususario vai precisar escolhar entre as duas e depois de escolhido vai dar uma breve explicação da qual escolheu, depois ira dar uma escolhar para digitar continuar ou voltar, para prosseguir para proxima etapa ou escolher outra Representação de Algoritmos.

    # Etapa 5: Deseja sair do sistema?
    print("-----------------------------------------------------------------------------------------------------------------")
    print("--- DESEJA SAIR DO SISTEMA? ---")
    resposta = input("\n(sim/não): ").strip().lower()

    if resposta == 'sim':
        print("\nEncerrando o sistema. Até logo!")
        print("-----------------------------------------------------------------------------------------------------------------")
        print("-----------------------------------------------------------------------------------------------------------------")
        break
    else:
        print("\nRetornando ao início do sistema...\n")
        print("-----------------------------------------------------------------------------------------------------------------")
        print("-----------------------------------------------------------------------------------------------------------------")
#Na etapa 5 vai perguntar se você vai continuar no sistema ou vai querer sair dele. Se querer continuar irá voltar para o início do sistema
