stuff = ("Charles", 7, 8.2, True, False, "Cats") #packing the tuple

print(stuff[2])
#stuff[2] = "Leaf" won't work bec immutable, can't reassign

# unpack the tuple
name, value1, value2, bool1, bool2, animal = stuff
print(bool1, bool2, animal)

#unpack the tuple but unsure how many items = variable length argument syntax *
person, number1, number2, *other = stuff
print(person, number1, number2, other) # other has turned into a list of the remaining variables

print(type(other)) #shows that "other" is list (with square brackets)

animals = "cat", "dog", "lion"
print(animals)

#if you want to create a tuple of 1 item, use round brackets and a comma
animals = ("cat",)
print(animals)