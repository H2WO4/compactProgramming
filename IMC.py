print("Vous mesurez {}cm et pesez {}kg votre IMC vaut {}".format((t := int(input("Taille : "))),
                                                                (m := int(input("Poids : "))),
                                                                round(m/(t/100)**2, 2)))