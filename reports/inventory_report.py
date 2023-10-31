import csv

class InventoryReport:
    def generate_report(self, warehouse, report_file_path='data/inventory_report.csv'):
        inventory_data = []

        for product_id, product in warehouse.products.items():
            product_info = product.get_product_info()
            inventory_data.append({
                'product_id': product_info['product_id'],
                'name': product_info['name'],
                'price': product_info['price'],
                'quantity': product_info['quantity']
            })

        with open(report_file_path, 'w', newline='') as report_file:
            fieldnames = ['product_id', 'name', 'price', 'quantity']
            report_writer = csv.DictWriter(report_file, fieldnames=fieldnames)
            report_writer.writeheader()
            for item in inventory_data:
                report_writer.writerow(item)

        print("Inventory Report:")
        print("-----------------")

        for item in inventory_data:
            print(f"{item['name']} - ID: {item['product_id']}, Price: ${item['price']:.2f}, Quantity: {item['quantity']}")

        print(f"Inventory report has been saved to {report_file_path}")
