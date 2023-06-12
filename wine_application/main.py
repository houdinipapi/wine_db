import json


# Function to save wine stock data to a JSON file
def save_stock_data(wine_stock):
    with open("wine_stock.json", "w") as file:
        json.dump(wine_stock, file)


# Function to load wine stock data from a JSON file
def load_stock_data():
    try:
        with open("wine_stock.json", 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Initialize wine stock dictionary
wine_stock = load_stock_data()


# Function to update wine stock after a sale
def update_stock(wine_stock, wine, quantity):
    if wine in wine_stock:
        current_stock = wine_stock[wine]
        if current_stock >= quantity:
            wine_stock[wine] -= quantity
            print(f"Sold {quantity} bottles of {wine}")
            print(f"Remaining stock of {wine}: {wine_stock[wine]}")
        else:
            print(f"Not enough stock of wine")
    else:
        print(f"{wine} is not available in the stock")


# Function to add new wine to the stock
def add_wine(wine_stock, wine, quantity):
    if wine in wine_stock:
        wine_stock[wine] += quantity
    else:
        wine_stock[wine] = quantity


# Function to display current wine stock
def display_stock(wine_stock):
    print("\nCurrent Wine Stock: ")
    for wine, stock in wine_stock.items():
        print(f"{wine}: {stock} bottles")


# Accept user input to manage wine stock
while True:
    print("\n1. Update Wine Stock")
    print("2. Add Wine to Stock")
    print("3. Display Wine Stock")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        wine = input("Enter the wine name: ")
        quantity = int(input("Enter the quantity sold: "))
        update_stock(wine_stock, wine, quantity)
    elif choice == "2":
        wine = input("Enter the wine name: ")
        quantity = int(input("Enter the quantity to add: "))
        add_wine(wine_stock, wine, quantity)
        print(f"Added {quantity} bottles of {wine} to the stock")
    elif choice == "3":
        display_stock(wine_stock)
    elif choice == "4":
        save_stock_data(wine_stock)
        print("Stock data saved. Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
