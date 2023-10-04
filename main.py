import json
def save_items(item_category,item_name,item_seller,item_dastavka,item_price,item_quantity,item_assessments,item_order):
    with open('item_databas.json','a') as file:
        data = {'item_category':item_category,
                'item_name':item_name, 
                'item_seller':item_seller,
                'item_dastavka':item_dastavka,
                'item_price':item_price,
                'item_quantity':item_quantity,
                'item_assessments':item_assessments,
                'item_order':item_order}
        json.dump(data,file)
        file.write('\n')

def load_database():
    try:
        with open('item_databas.json','r') as file :
            lines =  file.readlines()
            database = [json.loads(line) for line in lines] 
            return database
    except FileNotFoundError :
        return [] 
def get_user_input ():
    user_input = input("Enter the name of item: ")         
    return user_input
    
def ask_item(user_input, database):
    for entry in database:
        if entry['item_name'] == user_input:
            return entry
def filter_by_category(category,database)  :
    filtred_items=[]
    for entry in database:
        if entry['item_category'] == category :
            filtred_items.append(entry)  
        return filtred_items   

def total(price,database)  :
    for entry in database:
        if entry ['item_price'] == price:
            return entry    

def main(): 
    filter_choice = input("Do you to filter by category? yes/no: ").lower()
    if filter_choice == 'yes':
        category_to_filter = input("Enter the category to filter by: ")   
        database = load_database()
        filter_items = filter_by_category  (category_to_filter,database)  
        if filter_items:
            print(f"filtred news for category {category_to_filter}")
            for entry in filter_items:
                print(entry)
                choice = input("if you want to buy some itemsenter the (1)or exit(2): ")
                if choice == '1':
                    item_category = input("Enter the will buy category of item: ")
                    if item_category == database:
                        item_price = database[item_category]
                        quantity = int(input(f"Enter the quantity of {item_category} to buy: "))
                        total_cost = item_price * quantity
                        print(f"You bought {quantity}{item_category}(s)for {total_cost} so'm")
                    else:
                        print("Invalid product number . Please try again.")    
        else:
            print("No item found the spicified category")      
    else:          
        while True:
            database = load_database()
            user_input = get_user_input()
            items = ask_item(user_input,database)
            if items:
                print(items)
                break
            else:
                print("Sorry, I don't found this item name , if  you want to enter :")
                item_category = input("Enter the category: ")    
                item_name = input("Enter name of the item: ") 
                item_seller = input("Enter the item's seller :")  
                item_dastavka = input("Product delivery time:") 
                item_price = input("Product price:") 
                item_quantity = input("Items quantity")
                item_assessments = input("How many people liked this item: ")
                item_order = input("How many people ordered")
                save_items(item_category,item_name,item_seller,item_dastavka,item_price,item_quantity,item_assessments,item_order)
                print("Okay I saved new item name")

                continue_prompt = input("Again do you have info about new item yes/no")
                if continue_prompt.lower() == 'n':
                    continue

if __name__ == '__main__'   :
    main()

             
