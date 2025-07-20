def details(name, **kwargs):  #first arg is positional, next is variable length
    print("Name", name)

    print(type(kwargs))
    print(kwargs)

    if "height" in kwargs:   # will stop the code from crashing if details are not supplied on line 13
        print("Height", kwargs["height"])

    for key in kwargs:
        print(key, kwargs[key])

details("Sue", height=170, age=42)

#dict is like a hash map in Java, stores key/value pairs 