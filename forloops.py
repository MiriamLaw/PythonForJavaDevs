for i in range(5):
    print("For loop", i)

    print()

for i in range(2, 4):
    print("For loop", i)

for i in range(4, 10, 2):
    print("For loop", i)

for i in range(3, 0, -1):
    print("For loop", i)
    # to include 0, set middle parameter to -1 or it won't be counted
    # This loop uses range() with start=3, stop=0, and step=-1 as its arguments.