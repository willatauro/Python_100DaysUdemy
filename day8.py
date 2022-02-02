'''
def greet(a): #parameter
    print("Hello "+ a)
    print(f"Hello {a}")

name = input("What's your name:")
greet(name)  # argument


# Positional arguments
def greet_nam_loc (a,b):
    print(f"Hi {a}, how's the weather in {b}")

name = input("enter your name")
loc = input("enter your location")

greet_nam_loc(name,loc)

'''
#Keyword arguments 

def greet_nam_loc (a,b):
    print(f"Hi {a}, how's the weather in {b}")

name = input("enter your name")
loc = input("enter your location")

greet_nam_loc(a=name,b=loc)