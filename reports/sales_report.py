import csv

class SalesReport:
    def generate_report(self, warehouse, sales_file_path='data/sales_report.csv'):
        sales_data = []
        inventory_updates = {}

        total_revenue = 0  # Total revenue dari semua penjualan

        for product_id, product in warehouse.products.items():
            initial_quantity = product.get_product_info()['quantity']
            final_quantity = product.quantity
            quantity_sold = initial_quantity - final_quantity
            if quantity_sold > 0:
                revenue = product.price * quantity_sold
                total_revenue += revenue  # Menambahkan revenue ke total revenue
                sales_data.append({
                    'product_id': product_id,
                    'name': product.name,
                    'quantity_sold': quantity_sold,
                    'revenue': revenue
                })

                # Memasukkan pembaruan inventaris
                inventory_updates[product_id] = {
                    'product_id': product_id,
                    'name': product.name,
                    'quantity_sold': quantity_sold
                }

        with open(sales_file_path, 'w', newline='') as sales_file:
            fieldnames = ['product_id', 'name', 'quantity_sold', 'revenue']
            sales_writer = csv.DictWriter(sales_file, fieldnames=fieldnames)
            sales_writer.writeheader()
            
            # Menambahkan laporan penjualan untuk setiap transaksi
            for item in sales_data:
                sales_writer.writerow(item)

            # Menambahkan satu baris baru yang mencakup total penjualan
            total_quantity = sum(item['quantity_sold'] for item in sales_data)
            total_revenue_row = {
                'product_id': 'Total',
                'name': 'Total',
                'quantity_sold': total_quantity,
                'revenue': total_revenue
            }
            sales_writer.writerow(total_revenue_row)

        print("Sales Report:")
        print("--------------")

        for item in sales_data:
            print(f"{item['name']} - Sold: {item['quantity_sold']} units, Revenue: ${item['revenue']:.2f}")

        print(f"Total Revenue: ${total_revenue:.2f}")  # Mencetak total revenue keseluruhan

        # Mencetak pembaruan inventaris
        print("\nInventory Updates:")
        print("--------------")
        for update in inventory_updates.values():
            print(f"{update['name']} - Sold: {update['quantity_sold']} units")
