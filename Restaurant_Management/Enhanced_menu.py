# --------------------------------------------------
# Hotel Management System with GST (12%)
# --------------------------------------------------

# Dictionary to store food items and their prices
# Key   -> Food Item
# Value -> Price of the item
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

# GST rate (12%)
GST_RATE = 0.12

# -------------------------------
# Welcome Message
# -------------------------------
print("\n🍽️ Welcome to the Candy Crx Hotel 🍽️")
print("----------- MENU -----------")

# Display menu items using loop
for item, price in food_prices.items():
    print(f"{item} : {price}")

print("----------------------------")

# Variable to store total amount (before GST)
order_total = 0

# -------------------------------
# Order Taking Loop
# -------------------------------
while True:
    # Taking food item from user
    item = input("\nEnter the item you want to order: ").title()

    # Check if item exists in menu
    if item in food_prices:
        order_total += food_prices[item]
        print(f"✅ {item} added | Price: ₹{food_prices[item]}")
    else:
        print("❌ Item not available. Please order from the menu.")

    # Ask user if they want to add more items
    choice = input("Do you want to add another item? (Y/N): ").upper()

    if choice != "Y":
        break

# -------------------------------
# GST Calculation
# -------------------------------
gst_amount = order_total * GST_RATE          # Calculate GST
final_amount = order_total + gst_amount      # Final bill after GST

# -------------------------------
# Bill Summary
# -------------------------------
print("\n🧾 BILL SUMMARY")
print(f"Total Amount (Before GST): ₹{order_total}")
print(f"GST (12%): ₹{gst_amount:.2f}")
print(f"Final Amount to Pay: ₹{final_amount:.2f}")

print("\n🙏 Thank you for visiting Candy Crx Hotel!")
