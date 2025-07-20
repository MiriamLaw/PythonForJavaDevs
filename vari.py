def catalogue(name, *args):  #args is a tuple (type of list=non-modifiable array)
    # must prefix the whatever you call the variable length argument with an * and 
    # variable length arg must come last

    print("Type: ", type(args))

    print(name)

    if len(args) >= 1:
        print(args[0])

    for value in args:
        print(value)

catalogue("Trees", "oak", "ash", "linden")
catalogue("Blank") #won't crash because have the if statement