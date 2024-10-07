Selecaoclasse = int(input("Selecione a classe que gostaria de jogar!\n Digite1 para Guerreiro\n Digite 2 para mago\n Digite 3 para archer"))
if(Selecaoclasse == 1) :
    classe="Guerreiro"
if(Selecaoclasse== 2):
    classe = "Mago"
if (Selecaoclasse == 3):
    classe = "Archer"
else:
    classe= "invalida"

selecaoequip = int(input("Selecione o tipo de equipamento que deseja usar.\n Digite 1 para curto alcance\nDigie 2 para longo alance"))
if(selecaoequip)==1:
    equip="curto alcance"
elif(selecaoequip == 2):
    equip="longo alcance"
else:
    equip= "invalido"
    
print(f"voce escolheu a calasse {classe} para jogar com arma de {equip}")