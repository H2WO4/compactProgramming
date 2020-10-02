print("{} est divisible par {} : {}".format((x := int(input("x = "))),
                                            (n := int(input("n = "))),
                                            eval("lambda a, b: a % b == 0")(x, n)))