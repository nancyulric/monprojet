# creation des listes de Gandalf et Samuran

gandalf_list = [10, 11, 13, 30, 22, 11, 10, 33, 22, 22]

samuran_list = [23, 66, 12, 43, 12, 10, 44, 23, 12, 17]


# lecture des listes

for i, elt in enumerate(gandalf_list):
    print("In the {}e clash Gandalf scores {} points.".format(i, elt))

for i,  elt in enumerate(samuran_list):
    print("In the {}e clash Samuran scores {} points.".format(i, elt))


for i, elt in enumerate(gandalf_list):
    if elt > samuran_list[i]:
        print("Gandalf win : {} against {}".format(elt, samuran_list[i]))

for i, elt in enumerate(samuran_list):
    if elt > gandalf_list[i]:
        print("Samuran win : {} against {}".format(elt, gandalf_list[i]))









