#Hotel ManageMent SysTem Using Conditional Statement And Dictionary.
#Why Use Dictionary:? --- For Storing Item And There Price's In Key VAlue Pair's

#Defining The Value Of Items---

food_prices = {
    "Pizza": 250,
    "Burger": 120,
    "Pasta": 180,
    "Sandwich": 90,
    "Fried Rice": 150,
    "Noodles": 140,
    "Ice Cream": 80,
    "Coffee": 70,
    "Cake": 300,
    "French Fries": 100
}


# Greeting Customer-s
print("--Welcome to the Candy Crx Hotel--\n--Choose An Item To Order--")
print("Pizza : 250\nBurger : 120\nPasta : 180\nSandwich : 90\nFried Rice : 150\nNoodles : 140\nIce Cream : 80\nCoffee : 70\nCake : 300\nFrench Fries : 100")

order_total = 0

item_1 = input("Please Specify Your First Meal: ")
if item_1 in food_prices:
    order_total += food_prices[item_1]
    print(f"Your Food {item_1} has a been added to your order.")

else:
    print(f"Your Food {item_1} Is Not Available In Our Menu Order SomeThing From Menu.")


another_order = input("Do You Want To Add another Order? (Y/N): ")
if another_order == "Y":
    item_2 = input("Please Specify Your Second Meal: ")
    if item_2 in food_prices:
        order_total += food_prices[item_2]
        print(f"Your Food {item_2} has a been added to your order.")
    else:
        print("Order Two Is Not Available In Our Menu Order SomeThing From Menu.")
print(f"The Total Amount To Pay Is {order_total}")