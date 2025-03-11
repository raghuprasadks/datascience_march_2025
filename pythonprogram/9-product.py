class product:
    code: int
    name: str
    supplier: str
    price:int
    def info(self):
        print("Code: ", self.code)
        print("Name: ", self.name)
        print("Supplier: ", self.supplier)
        print("Price: ", self.price)
prodcut1=product()
prodcut1.code=101
prodcut1.name="Laptop"
prodcut1.supplier="HP"
prodcut1.price=45000    
prodcut1.info()

class productnew():
    def __init__(self, code, name, supplier, price):
        self.code = code
        self.name = name
        self.supplier = supplier
        self.price = price
    def info(self):
        print("Code: ", self.code)
        print("Name: ", self.name)
        print("Supplier: ", self.supplier)
        print("Price: ", self.price)

prodcut2=productnew(102, "Mobile", "Samsung", 25000)
prodcut2.info()

#prodcut3=productnew()


class cart():
    def __init__(self):
        self.items = []
    def add_item(self, product):
        self.items.append(product)
    def display_cart(self):
        for product in self.items:
            product.info()
    def checkout(self):
        total=0
        for product in self.items:
            total+=product.price
        print("Total: ", total)
cart1=cart()
product1=productnew(101, "Tablet", "Apple", 35000)
product2=productnew(102, "Mobile", "Samsung", 25000)
product3=productnew(103, "Laptop", "HP", 45000)
cart1.add_item(product1)
cart1.add_item(product2)
cart1.add_item(product3)
cart1.display_cart()
cart1.checkout()

