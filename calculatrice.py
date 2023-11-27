print("bienvenue dans la calculatrice\n")
nb_cal_user = int(input("combien de calcule sont prévu? :"))


for a in range(int(nb_cal_user)):
    
    #le user choisie quel calcule il veut faire
    #savoir si le user veut faire un autre calcule  
    print("quel type de calcule vous voulez faire :")
    print("1 = addition")
    print("2 = soustraction")
    print("3 = multiplication")
    print("4 = division")
    print("5 = racine carré")

    user_cal_choix = int(input(" quel chiffre choisiser vous :  "))

    if user_cal_choix == (1) : 
 
     user_add =int(input("quel est le primer chiffre : "))
     user_add2 =int(input("quel est le deuxiemme chiffre : "))
     resulta_add = user_add + user_add2
     print("le resultat de l'addition est :",resulta_add)
    
    elif user_cal_choix == (2): 
        user_sous =int(input("quel est le primer chiffre : "))
        user_sous2 =int(input("quel est le deuxiemme chiffre : "))
        resulta_add = user_sous - user_sous2
        print("le resultat de l'addition est :",resulta_add)

    elif user_cal_choix ==(3): 
        user_mul =int(input("quel est le primer chiffre : "))
        user_mul2 =int(input("quel est le deuxiemme chiffre : "))
        resulta_add = user_mul * user_mul2
        print("le resultat de l'addition est :",resulta_add)


    elif user_cal_choix == (4) :
        user_div =int(input("quel est le primer chiffre : "))
        user_div2 =int(input("quel est le deuxiemme chiffre : "))
        resulta_add = user_div / user_div2
        print("le resultat de l'addition est :",resulta_add)

    elif user_cal_choix == (5):
        user_rc =int(input("quel est le chiffre : "))
        resulta_add = user_rc ** 0.5
        print("le resultat de l'addition est :",resulta_add)
    print("")
