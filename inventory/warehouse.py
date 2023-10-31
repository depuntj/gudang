import csv

from inventory.product import Product

class Warehouse:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if isinstance(product, Product):
            self.products[product.product_id] = product

    def remove_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]

    def get_product(self, product_id):
        return self.products.get(product_id, None)

    def load_products(self, file_path):
        products_data = {}
        with open(file_path, 'r') as product_file:
            product_reader = csv.DictReader(product_file)
            for row in product_reader:
                product_id = row['product_id']
                product_data = {
                    'name': row['name'],
                    'price': float(row['price']),
                    'quantity': int(row['quantity']),
                }
                products_data[product_id] = product_data
        return products_data

    def load_inventory(self, file_path):
        inventory_data = {}
        with open(file_path, 'r') as inventory_file:
            inventory_reader = csv.DictReader(inventory_file)
            for row in inventory_reader:
                product_id = row['product_id']
                inventory_data[product_id] = int(row['quantity'])
        return inventory_data

    def sell_product(self, product_id, quantity_sold):
        if product_id in self.products:
            product = self.products[product_id]
            if product.sell(quantity_sold):
                print(f"Sold {quantity_sold} units of {product.name}.")
            else:
                print(f"Insufficient stock for {product.name}.")
        else:
            print(f"Product with ID {product_id} not found in the warehouse.")

    def list_products(self):
        for product_id, product in self.products.items():
            print(product)

    def update_inventory(self, file_path, inventory_data):
        with open(file_path, 'w', newline='') as inventory_file:
            inventory_writer = csv.DictWriter(inventory_file, fieldnames=['product_id', 'quantity'])
            inventory_writer.writeheader()
            for product_id, quantity in inventory_data.items():
                inventory_writer.writerow({'product_id': product_id, 'quantity': quantity})