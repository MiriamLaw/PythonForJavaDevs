
def names():
    return "Bob", "Sue", "Pete" #this is called "packing a tuple"

name1, name2, name3 = names() #unpacking the tuple

print(name1, name2, name3) #this will end up as a tuple (put type() around names and see)