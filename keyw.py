def calculate_area(width, height, length=1):
    return width * height * length

# area = calculate_area(width=2, height=3, length=6)
area = calculate_area(2, length=6, height=8) #positional argument not named has to be 
#aligned with first arg in def, then others can be named and in any order, also all can be 
# in any order if all named
print(area)
