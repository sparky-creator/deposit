# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")

def greet(name,greeting):
    print(f"{greeting} {name}")

greet("Hanna", "Yo")

def greet_with(name="Hanna", location="NY"):
    print(f"Hello {name}")
    print(f"What is it like in {location}")
    print(f"{location}")

greet_with("Euna", "NY")

greet_with(location="haha",name="euna")
