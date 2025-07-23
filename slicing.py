animals = ("cat", "dog", "giraffe", "lion", "elephant", "badger")

print(animals[2]) #thhink of this as a slice
print(animals[1:4]) #this slice will give indices at 1, 2, and 3 (but not include 4)
print(animals[-1]) #will give badger as the last index (called negative indices)
print(animals[-4:-1]) #a slice with negative indices, note cannot use a 0 with negative indices
print(animals[1:-1:2]) #use with a step size at the end of the slice, (start, end, step size)
print(animals[:3]) #step size left out (defaults to 1), start left out (defaults to "cat"), our :3 represents end of range
print(animals[::2]) #missed start and end of range (defaults to entire tuple) so 2 represents step size
print(animals[::]) #still valid, start defaults to first index, end defaults to entire tuple, step size defaults to 1
