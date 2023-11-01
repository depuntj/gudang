class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
    def __str__(self):
        return f"{self.product_id}: {self.name} - Price: ${self.price:.2f}, Quantity: {self.quantity}"

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

    def get_product_info(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
        }

    def sell(self, quantity_sold):
        if quantity_sold <= self.quantity:
            self.quantity -= quantity_sold
            return True
        else:
            return False
    import pandas as pd

    def load_products(file_path):
        try:
            products_df = pd.read_csv(file_path)
            products_data = {}
            for index, row in products_df.iterrows():
                product_id = row['product_id']
                name = row['name']
                price = row['price']
                quantity = row['quantity']
                products_data[product_id] = Product(product_id, name, price, quantity)
            return products_data
        except FileNotFoundError:
            print(f"File {file_path} not found.")
            return {}
