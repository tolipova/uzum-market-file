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
def buyer(item_name,item_quantity,item_price,database) :
    name = input("Enter the name will buy of item: ")   
    if name == database[item_name]:
        quantity = int(input(f"enter the quantity of {name} to buy "))
        if quantity > item_quantity:
            print("Error! this quantity more a lot")
        elif quantity <= item_quantity:
            total_cost = item_price * quantity
            print(f"You bought {quantity}{item_name}(s)for {total_cost} so'm")
        else:
            print("Error!!")    
            

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
        else:
            print("No item found the spicified category")      
    else:          
        while True:
            choice = input("Choosing you seller or buyyer: ").lower()
            if choice == 'seller':
                print(main)
            elif choice == 'buyyer' :
                print(buyer) 
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

             
