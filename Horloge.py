print("Le temps {}h:{}m:{}s correspond à {}s".format(h := int(input("Heure : ")),
                                                    m := int(input("Minute : ")),
                                                    s := int(input("Seconde : ")),
                                                    3600 * h + 60 * m + s))