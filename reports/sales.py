import pandas as pd
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
        sales_data = {
            'product_id': [product_id],
            'name': [name],
            'quantity_sold': [quantity_sold],
            'price': [price],
        }

        sales_df = pd.DataFrame(sales_data)
        
        try:
            existing_sales = pd.read_csv(self.sales_file_path)
            updated_sales = pd.concat([existing_sales, sales_df], ignore_index=True)
            updated_sales.to_csv(self.sales_file_path, index=False)
        except FileNotFoundError:
            sales_df.to_csv(self.sales_file_path, index=False)

    def generate_sales_report(self):
        print("Sales Report:")
        print("--------------")

        try:
            sales_df = pd.read_csv(self.sales_file_path)
            total_revenue = (sales_df['quantity_sold'] * sales_df['price']).sum()

            for index, row in sales_df.iterrows():
                print(f"{row['name']} - Sold: {row['quantity_sold']} units, Revenue: ${row['price'] * row['quantity_sold']:.2f}")

            print(f"Total Revenue: ${total_revenue:.2f}")
        except FileNotFoundError:
            print("No sales data found.")

# Contoh penggunaan
if __name__ == "__main__":
    sales_manager = Sales()
    sales_manager.sell_product(warehouse, "P7", 20)
    sales_manager.generate_sales_report()
