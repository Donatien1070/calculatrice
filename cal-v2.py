print("Bienvenue dans la calculatrice\n")
nb_cal_user = int(input("Combien de calculs sont prévus? : "))

for _ in range(nb_cal_user):
    print("Quel type de calcul voulez-vous faire :")
    print("1 = addition")
    print("2 = soustraction")
    print("3 = multiplication")
    print("4 = division")
    print("5 = racine carrée")

    user_cal_choix = int(input("Quel chiffre choisissez-vous : "))

    if user_cal_choix in (1, 2, 3, 4):
        user_num1 = int(input("Quel est le premier chiffre : "))
        user_num2 = int(input("Quel est le deuxième chiffre : "))

        if user_cal_choix == 1:
            result = user_num1 + user_num2
        elif user_cal_choix == 2:
            result = user_num1 - user_num2
        elif user_cal_choix == 3:
            result = user_num1 * user_num2
        elif user_cal_choix == 4:
            result = user_num1 / user_num2

        print(f"Le résultat est : {result}")

    elif user_cal_choix == 5:
        user_num = int(input("Quel est le chiffre : "))
        result = user_num ** 0.5
        print(f"Le résultat est : {result}")

    print("")
