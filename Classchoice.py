print ("Olá, seja bem vindo ao nosso RPG\n Agora escoheremos sua classe\n 1- Barbaro\n 2- Mago\n 3- Arqueiro ")
classe = int (input("Qual classe deseja esolher ? "))

if classe == 1:
    print ("Você escoheu Barbaro")
elif classe == 2:
    print ("você escolheu Mago")
elif classe == 3:
    print ("você escolheu Arqueiro")
else:
    print ( "Nao entendemos sua escolha, por favor repita com uma opção válida")    