print("La différence entre {}h:{}m:{}s et {}h:{}m:{}s correspond à {}s".format(h := int(input("Heure : ")),
                                                                                m := int(input("Minute : ")),
                                                                                s := int(input("Seconde : ")),
                                                                                h2 := int(input("Heure 2 : ")),
                                                                                m2 := int(input("Minute 2 : ")),
                                                                                s2 := int(input("Seconde 2 : ")),
                                                                                abs(h - h2) * 3600 + abs(m - m2) * 60  + abs(s - s2)))