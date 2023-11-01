import pandas as pd

def load_inventory(file_path):
    try:
        inventory_df = pd.read_csv(file_path)
        inventory_data = inventory_df.set_index('product_id').to_dict()['quantity']
        return inventory_data
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return {}

def update_inventory(file_path, inventory_data):
    with open(file_path, 'w', newline='') as inventory_file:
        inventory_writer = csv.DictWriter(inventory_file, fieldnames=['product_id', 'quantity'])
        inventory_writer.writeheader()
        for product_id, quantity in inventory_data.items():
            inventory_writer.writerow({'product_id': product_id, 'quantity': quantity})
