class Product:
    def __init__(self, name, price, brand, seller):
        self.name = name
        self.price = price
        self.brand = brand
        self.seller = seller
    def display_product(self):
        print("Product Name:", self.name)
        print("Price:", self.price)
        print("Brand:", self.brand)
        print("Seller:", self.seller)
class CottonClothes(Product):
    def __init__(self, name, price, brand, seller, wash_instruction):
        super().__init__(name, price, brand, seller)
        self.wash_instruction = wash_instruction
    def display_details(self):
        self.display_product()
        print("Wash Instruction:", self.wash_instruction)
class SilkClothes(Product):
    def __init__(self, name, price, brand, seller, care_instruction):
        super().__init__(name, price, brand, seller)
        self.care_instruction = care_instruction
    def display_details(self):
        self.display_product()
        print("Care Instruction:", self.care_instruction)
cotton = CottonClothes(
    "Cotton Shirt",
    799,
    "Allen Solly",
    "ABC Fashion Store",
    "Machine wash in cold water"
)
silk = SilkClothes(
    "Silk Saree",
    4999,
    "Kanchi Silks",
    "XYZ Silk House",
    "Dry clean only"
)
print("Cotton Clothes")
cotton.display_details()
print("Silk Clothes")
silk.display_details()

