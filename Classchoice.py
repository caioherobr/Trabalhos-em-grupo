print ("Olá, seja bem vindo ao nosso RPG\n Agora escolheremos sua classe\n 1- Barbaro\n 2- Mago\n 3- Arqueiro ")
classe = int (input("Qual classe deseja esolher ? "))

if classe == 1:
    classe = ('Barbaro')
    print ("Você escoheu Barbaro")
elif classe == 2:
    classe = ('Mago')
    print ("você escolheu Mago")
elif classe == 3:
    classe = ('Arqueiro')
    print ("você escolheu Arqueiro")
else:
    print ( "Nao entendemos sua escolha, por favor repita com uma opção válida")

equip = int(input('Qual tipo de equipamento deseja ultilizar?: \n1)curto alcance\n2)longo alcance '))

if equip == 1:
    equip = ('curto alcance')

elif equip == 2:
    equip = ('longo alcance')

else:
    print('escolha invalida, por favor escolha um equipamento existente')


print(f'Então vocÊ decidiu usar a classe {classe} e seu equipamento é de {equip}')