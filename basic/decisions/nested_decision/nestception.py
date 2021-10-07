print("Where should i look?")
places = input()
if places == 'in the bedroom':
    print("Where in the bedroom should i look?")
    bedroom = input()
    if bedroom =='in the cupboard':
        print("Found some mess but no battery.")
    else:
        print("Found some shoes but no battery.")

elif places == 'in the bathroom':
    print("Where in the bathroom should i look?")
    bathroom = input()
    if bathroom == 'in the bathtub':
        print("Found a rubber duck but no battery.")
    else:
        print("Found a wet surface but no battery.")

elif places == 'in the lab':
    print("Where in the lab should i look?")
    lab = input()
    if lab == 'on the table':
        print("Yes! I found my battery!")
    else:
        print("found some tools but no battery")

else:
    print("I do not know where that is but i will keep looking.")


print("Program ended!")

