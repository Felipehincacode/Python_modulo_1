#inventory software for a store "The hope"
import time #i use this  for simulate processing time

shop = {
    "inventory": [
        {
          "item_name": "cocacola", #string
          "item_amount" : 34,      #int
          "item_price" : 7500.0    #float
        },
        {
          "item_name": "battery", #string
          "item_amount" : 15,      #int
          "item_price" : 2500.0    #float 
        },
        {
          "item_name": "toilet paper", #string
          "item_amount" : 34,      #int
          "item_price" : 3500.0    #float 
        },
        {
          "item_name": "frozen_pizza", #string
          "item_amount" : 50,      #int
          "item_price" : 1500.0    #float 
        },
        {
          "item_name": "rice", #string
          "item_amount" : 150,      #int
          "item_price" : 4500.0    #float 
        }      

            ]  

     }

#Auxiliary functions
#i dont want to repeat code so i made a function that calls another function 

def ask_for_create():  #ask the user if want to create the item, if the answer is yes call the create item function
    ask_for_create = input(" 🤔🤔 Do you want to create it?  🤔🤔 (y/n)").lower().strip() 
    if ask_for_create == "y":
        
        print("The system will send you to the item creation module. 🫡🫡 ")
        time.sleep(1)
        create_item() #
    else:
        print("exiting from search module")


def create_item(): #checked
    item_inventory = shop["inventory"]
    name_item = input("Enter the name of the item you want to add to inventory 🏷️🏷️  ").lower().strip()
    time.sleep(1)
    while True:
        try:
            item_amount = int(input('Enter the number of products you want to add to inventory. 📥📥   '))
            break
        except ValueError:
            print("Please enter a numeric value")
            continue
    time.sleep(1)
    item_price = float(input('enter the value of the product 💲💲  '))

    item_creator = {
          "item_name": name_item , "item_amount" : item_amount , "item_price" : item_price}
    item_inventory.append(item_creator)
    time.sleep(1)
    print(f"{item_creator} Succesfully charged on system 🗃️🗃️  ")


def check_products_in_inventory(): #checked
    name_item = input("Enter the name of the product you want to search for in the inventory: ➡️ ").lower().strip()
    item_inventory = shop["inventory"]
    print("Processing  your query  🔍🔍🔍")
    time.sleep(1)
    
    for i in item_inventory:
        if name_item == i["item_name"]:
            print("The item is in our inventory!!!")
            time.sleep(1)
            print(f'▶️ Item name: {i["item_name"]}◀️ \n▶️ Item amount: {i["item_amount"]} ◀️\n▶️ Item price: {i["item_price"]}◀️  ')
            return
    print(" 🚫 Sorry that item name doesn't exist 🚫")
    time.sleep(1)
    ask_for_create()


def update_item_price():
    name_item = input("Enter the name of the product whose price you want to update: ➡️ ").lower().strip()
    item_inventory = shop["inventory"]
    print("Processing  your query  🔍🔍🔍")
    time.sleep(1)
    
    for i in item_inventory:
        if name_item == i["item_name"]:
            print("Item found")
            time.sleep(1)
            uptade_price = float(input(f"Enter the new price for {i["item_name"]}"))
            i["item_price"]= uptade_price
            print("The item price was updated successfully ")
            print(f'▶️ Item name: {i["item_name"]}◀️ \n▶️ Item amount: {i["item_amount"]} ◀️\n▶️ Item price: {i["item_price"]}◀️  ')
            return
    
    print(" 🚫 Sorry that item name doesn't exist 🚫")
    time.sleep(1)
    ask_for_create()

def delete_item_outstock():
    name_item = input("Enter the name of the product do you want delete from the inventory: ➡️ ").lower().strip()
    item_inventory = shop["inventory"]
    print("Processing  your query  🔍🔍🔍")
    time.sleep(1)
    
    for i in item_inventory:
        if name_item == i["item_name"]:
            print(f"Item {name_item} found")
            if i["item_amount"] == 0:
                print(f"the item: {i['item_name']} is ready to delete ")
                confirm_delete = input('Are you sure you want to delete the file? (y/n) \n⚠️⚠️This action is irreversible.⚠️⚠️ \n').lower().strip()
                if confirm_delete == 'y':
                    del item_inventory.remove[i]
                    print("the item was deleted succesfully")
                    return
                else:
                    print("Ok, the item wasnt deleted")
                    return
            else:
                print("You cannot delete the item because there are still products in the inventory.")
                return
    
    print(" 🚫 Sorry that item name doesn't exist 🚫")
    time.sleep(1)
    ask_for_create()



def price_of_all_inventary():
    item_inventory = shop["inventory"]
    if not item_inventory:
        print("El inventario está vacío. Valor total: 0")
        return
    total_value = sum(map(lambda item: item["item_price"] * item["item_amount"], item_inventory))
    print(f"El valor total de todo el inventario es: {total_value}")
    return
    
        

    
def main():
    while True: 
        print("\n--- Hope's inventory sistem ---")
        print("1. Add item")
        print("2. Consult item")
        print("3. edit price of an item")
        print("4. delete a product outstore")
        print("5. all prince inventory")
        print("6. exit") # Opción para terminar el programa

        opcion = input("Enter the number of the option you want to choose ").strip() # Leer la opción del usuario

        if opcion == "1":
            create_item()
        elif opcion == "2":
            check_products_in_inventory()
        elif opcion == "3":
            update_item_price()
        elif opcion == "4":
            delete_item_outstock()
        elif opcion == "5":
            price_of_all_inventary()
        elif opcion == "5":
            print("exiting program")
            break 
        else:
            print("No valid option")

if __name__ == "__main__":
    main()
