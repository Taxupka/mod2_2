my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
nom = 0
while nom < len(my_list):
    if my_list[nom] > 0:
        print(my_list[nom])

    if my_list[nom] < 0:
        break
    nom += 1