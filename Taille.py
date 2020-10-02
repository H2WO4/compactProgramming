print("Votre taille est {}".format(eval("lambda taillePère, tailleMère,garçon: \
                                        [(taillePère + tailleMère - 13) / 2, (taillePère + tailleMère + 13) / 2][garçon]") \
    (int(input("Taille de ton père (en cm): ")),
    int(input("Taille de ta mère (en cm): ")),
    eval(input("Est tu un garçon ? (True/False) : ")))))