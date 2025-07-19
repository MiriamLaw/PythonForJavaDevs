# and, not, or
# True, False

#if True:
#   print("This will always run.")

#if False:
#    print("This will never run.")

raining = False
temperature = 18

if temperature > 19 and not raining:
    print("Weather fine")
elif not raining: 
    print("At least it's dry")
else: 
    print("Stay indoors")

mood = "good" if not raining else "bad"
print(mood)



x = 3

if x > 0:
    print("Positive number")

while x > 0:
    print(x)
    x -= 1