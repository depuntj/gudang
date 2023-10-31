import csv

def load_inventory(file_path):
    inventory_data = {}
    with open(file_path, 'r') as inventory_file:
        inventory_reader = csv.DictReader(inventory_file)
        for row in inventory_reader:
            product_id = row['product_id']
            inventory_data[product_id] = int(row['quantity'])
    return inventory_data

def update_inventory(file_path, inventory_data):
    with open(file_path, 'w', newline='') as inventory_file:
        inventory_writer = csv.DictWriter(inventory_file, fieldnames=['product_id', 'quantity'])
        inventory_writer.writeheader()
        for product_id, quantity in inventory_data.items():
            inventory_writer.writerow({'product_id': product_id, 'quantity': quantity})
