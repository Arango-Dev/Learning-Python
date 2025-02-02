"""functions"""


def hello(name, lastname="Optional"):
    print("Hello World!")
    print(f"Hola {name} {lastname}")


hello("Pepe", "Perez")
hello("Juan")
hello(lastname="Testing", name="Named arguments")
