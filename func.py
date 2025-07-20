def calculate_area(width, height, length=1):
  #  pass #allows the method above to compile while you figure out what to pass
    return width * height * length
# area = calculate_area(2, 3, 6)
area = calculate_area(2, 3) #coincides with declaring a default argument for length above
#default params must come at end of positional arguments, unless all have default values 
print(area)