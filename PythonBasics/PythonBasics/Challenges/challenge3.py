#Find a meal without spam in it and print out the ingredients of that meal.

menu =[]
menu.append(["egg","spam","bacon"])
menu.append(["egg","sausage","bacon"])
menu.append(["egg","spam"])
menu.append(["egg","bacon", "spam"])
menu.append(["egg","bacon","sausage", "spam"])
menu.append(["spam","bacon","sausage","spam"])
menu.append(["spam","egg","spam", "spam", "bacon", "spam"])
menu.append(["spam","egg","sausage", "spam"])

for meal in menu:
    if not "spam" in meal:
        for value in meal:
            print(value)