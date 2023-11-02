import csv
from inventory.product import Product
from inventory.warehouse import Warehouse
from reports.sales import Sales
from reports.inventory_report import InventoryReport

def load_products(file_path):
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

def main():
    # Memuat produk dari file products.csv
    products_data = load_products('data/products.csv')
    
    # Membuat produk berdasarkan data yang dimuat
    products = {product_id: Product(product_id, data['name'], data['price'], data['quantity']) for product_id, data in products_data.items()}
    
    # Membuat gudang dan menambahkan produk ke dalamnya
    warehouse = Warehouse()
    for product in products.values():
        warehouse.add_product(product)
    
    # Membuat objek Sales dari sales.py
    sales_manager = Sales()

    # Melakukan penjualan
    sales_manager.sell_product(warehouse, "P9", 1) 

    
    # Membuat laporan penjualan
    sales_manager.generate_sales_report()
    
    # Membuat objek InventoryReport dan menghasilkan laporan inventaris
    inventory_report = InventoryReport()
    inventory_report.generate_report(warehouse)
    # melakukan update data berdasarkan laporan penjualan dalam sales_report.csv
    warehouse.update_product_from_sales_report('data/sales_report.csv')
    

if __name__ == "__main__":
    main()
