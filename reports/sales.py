import csv

class Sales:
    def __init__(self, sales_file_path='data/sales_report.csv'):
        self.sales_file_path = sales_file_path

    def sell_product(self, warehouse, product_id, quantity_sold):
        if product_id in warehouse.products:
            product = warehouse.get_product(product_id)
            if product.sell(quantity_sold):
                self.update_sales_report(product_id, product.name, quantity_sold, product.price)
                print(f"Sold {quantity_sold} units of {product.name}.")
            else:
                print(f"Insufficient stock for {product.name}.")
        else:
            print(f"Product with ID {product_id} not found in the warehouse.")

    def update_sales_report(self, product_id, name, quantity_sold, price):
        with open(self.sales_file_path, 'a', newline='') as sales_file:
            sales_writer = csv.writer(sales_file)
            sales_writer.writerow([product_id, name, quantity_sold, price])

    def generate_sales_report(self):
        print("Sales Report:")
        print("--------------")

        total_revenue = 0
        with open(self.sales_file_path, 'r') as sales_file:
            sales_reader = csv.reader(sales_file)
            for row in sales_reader:
                product_id, name, quantity_sold, price = row
                quantity_sold = int(quantity_sold)
                price = float(price)
                revenue = quantity_sold * price
                total_revenue += revenue
                print(f"{name} - Sold: {quantity_sold} units, Revenue: ${revenue:.2f}")

        print(f"Total Revenue: ${total_revenue:.2f}")