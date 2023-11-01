import pandas as pd

class InventoryReport:
    def __init__(self, inventory_file_path='data/inventory.csv'):
        self.inventory_file_path = inventory_file_path

    def generate_report(self, warehouse, report_file_path='data/inventory_report.csv'):
        # Memuat data inventaris dari file inventory.csv
        try:
            inventory_df = pd.read_csv(self.inventory_file_path, index_col='product_id')
        except FileNotFoundError:
            print(f"File {self.inventory_file_path} not found.")
            inventory_df = pd.DataFrame(columns=['quantity'])

        for product_id, product in warehouse.products.items():
            initial_quantity = inventory_df.loc[product_id, 'quantity'] if product_id in inventory_df.index else 0
            final_quantity = product.quantity
            quantity_sold = initial_quantity - final_quantity

            if quantity_sold > 0:
                inventory_df.loc[product_id, 'quantity'] = final_quantity

        # Menyimpan data inventaris yang telah diperbarui ke inventory.csv
        inventory_df.to_csv(self.inventory_file_path)

        # Menyimpan laporan inventaris yang telah diperbarui ke inventory_report.csv
        inventory_df.to_csv(report_file_path, header=True, index=True)

        print("Inventory Report:")
        print("-----------------")

        for index, row in inventory_df.iterrows():
            print(f"Product ID: {index}, Quantity: {row['quantity']}")

# Contoh penggunaan
if __name__ == "__main__":
    inventory_report = InventoryReport()
    inventory_report.generate_report(warehouse)
