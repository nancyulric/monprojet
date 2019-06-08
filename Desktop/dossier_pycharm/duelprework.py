gandalf_spell_power_list = [10, 11, 13, 30, 22, 11, 10, 33, 22, 22]
print(gandalf_spell_power_list)

saruman_spell_power_list = [23, 66, 12, 43, 12, 10, 44, 23, 12, 17]

i=0
while i <len(gandalf_spell_power_list):
    print(gandalf_spell_power_list[i])
    i +=1

for elt in gandalf_spell_power_list:
    print(elt)

for i, elt in enumerate(gandalf_spell_power_list):
    print("au {}e clash, Gandalf marque {} de points.".format(i,elt))

for elt in enumerate(gandalf_spell_power_list):
    print(elt)

# Assign 0 to each variable that stores the victories
gandalf_spell_power_list = [10, 11, 13, 30, 22, 11, 10, 33, 22, 22]

gandalf_spell_power_list[0:2]=[0, 0]
print(gandalf_spell_power_list)

gandalf_spell_power_list[3]=0
print(gandalf_spell_power_list)

gandalf_spell_power_list[6]=0
print(gandalf_spell_power_list)

gandalf_win_list = [0, 0, 13, 0, 22, 11, 0, 33, 22, 22]

saruman_spell_power_list = [23, 66, 12, 43, 12, 10, 44, 23, 12, 17]

saruman_spell_power_list[2] = 0
saruman_spell_power_list[4:6] = [0, 0]
saruman_spell_power_list[7:10] = [0, 0, 0]
print(saruman_spell_power_list)

saruman_win_list = [23, 66, 0, 43, 0, 0, 44, 0, 0, 0]

# Execution of spell clashes

gandalf_win_list = [0, 0, 13, 0, 22, 11, 0, 33, 22, 22]
for i, number in enumerate(gandalf_win_list):
    if number > 0:
        print("The {}e clash is won by Gandalf with {} points.".format(i, number))
    else:
        print("The {}e clash is won by Samuran.".format(i))

saruman_win_list = [23, 66, 0, 43, 0, 0, 44, 0, 0, 0]
for i, number in enumerate(saruman_win_list):
    if number > 0:
        print("The {}e clash is won by Samuran with {} points.".format(i, number))
    else:
        print("The {}e clash is won by Gandalf.".format(i))

# We check who has won, do not forget the possibility of a draw.
# Print the result based on the winner.

gandalf_win_list = [0, 0, 13, 0, 22, 11, 0, 33, 22, 22]
gandalf_win_list.sort()
print(gandalf_win_list)
del gandalf_win_list[0:4]
print(gandalf_win_list)
print(len(gandalf_win_list))
print("Gandalf won 6 clashes.")

saruman_win_list = [23, 66, 0, 43, 0, 0, 44, 0, 0, 0]
saruman_win_list.sort()
print(saruman_win_list)
del saruman_win_list[0:6]
print(saruman_win_list)
print(len(saruman_win_list))
print("Samuran won 4 clashes.")
print("Gandalf is the winner.")








