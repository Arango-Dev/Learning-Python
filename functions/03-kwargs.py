def get_product(**data):
    print(data)
    print(f"{data["id"]} {data["price"]}")


get_product(id="25", name="Product", price=20)
