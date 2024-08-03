shopping_list = [list]

action = input('''

Select an action you'd like to perform:


1 - Add to shopping list

2 - Remove from shopping list

3 - Print out the list1

''')

if action == '1':
    list = input("What would you like to add?")
    shopping_list.append(list)
    print("Adding", (list), "to shopping list")

if action == '2':
    list = input("What would you like to subtract?")
    shopping_list.remove(list)
    print("Removing", (list), "from the shopping list.")

if action == '3':
    print(shopping_list)