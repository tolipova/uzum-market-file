import json

def save_items(item_category, item_name, item_seller, item_dastavka, item_price, item_quantity, item_assessments, item_order):
    with open('item_database.json', 'a') as file:
        data = {
            'item_category': item_category,
            'item_name': item_name,
            'item_seller': item_seller,
            'item_dastavka': item_dastavka,
            'item_price': item_price,
            'item_quantity': item_quantity,
            'item_assessments': item_assessments,
            'item_order': item_order
        }
        json.dump(data, file)
        file.write('\n')

def load_database():
    try:
        with open('item_database.json', 'r') as file:
            lines = file.readlines()
            database = [json.loads(line) for line in lines]
            return database
    except FileNotFoundError:
        return []

def get_user_input():
    user_input = input("Enter the name of item: ")
    return user_input

def ask_item(user_input, database):
    for entry in database:
        if entry['item_name'] == user_input:
            return entry

def filter_by_category(category, database):
    filtered_items = []
    for entry in database:
        if entry['item_category'] == category:
            filtered_items.append(entry)
    return filtered_items

def seller():
    item_category = input("Enter the category of the item: ")
    item_name = input("Enter the name of the item: ")
    item_seller = input("Enter the seller's name: ")
    item_dastavka = input("Enter product delivery time: ")
    item_price = int(input("Enter the product price: "))  # Convert to int
    item_quantity = int(input("Enter the item quantity: "))  # Convert to int
    item_assessments = int(input("Enter how many people liked this item: "))  # Convert to int
    item_order = int(input("Enter how many people ordered: "))  # Convert to int

    # Save the item to the database
    save_items(item_category, item_name, item_seller, item_dastavka, item_price, item_quantity, item_assessments, item_order)
    print("Item saved successfully.")

def buyer(item_name, item_quantity, item_price, database):
    name = input("Enter the name of the item to buy: ")
    for entry in database:
        if entry['item_name'] == name:
            quantity = int(input(f"Enter the quantity of {name} to buy: "))
            if quantity > int(entry['item_quantity']):
                print("Error! This quantity is more than available.")
            elif quantity <= int(entry['item_quantity']):
                total_cost = int(entry['item_price']) * quantity
                print(f"You bought {quantity} {name}(s) for {total_cost} so'm.")
            else:
                print("Error!")

def main():
    filter_choice = input("Do you want to filter by category? (yes/no): ").lower()
    if filter_choice == 'yes':
        category_to_filter = input("Enter the category to filter by: ")
        database = load_database()
        filtered_items = filter_by_category(category_to_filter, database)
        if filtered_items:
            print(f"Filtered items for category {category_to_filter}:")
            for entry in filtered_items:
                print(entry)
        else:
            print("No items found for the specified category")
            
    else:
        while True:
            choice = input("Choose 'seller' or 'buyer': ").lower()
            if choice == 'seller':
                seller()  # Call the seller function
            elif choice == 'buyer':
                database = load_database()
                user_input = get_user_input()
                item = ask_item(user_input, database)
                if item:
                    item_name = item['item_name']
                    item_price = item['item_price']
                    item_quantity = item['item_quantity']
                    buyer(item_name, item_quantity, item_price, database)
                else:
                    print("Item not found.")
            else:
                print("Invalid choice. Please choose 'seller' or 'buyer'.")

if __name__ == '__main__':
    main()
