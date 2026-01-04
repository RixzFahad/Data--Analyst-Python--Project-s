print("\n========== FLAT EXPENSE MANAGEMENT SYSTEM ==========\n")

# ----- INPUT SECTION -----
Rent = float(input("Enter Total Flat Rent = ₹"))
Food = float(input("Enter Total Food Expenses = ₹"))
Elect_Unit = float(input("Enter Electricity Units Consumed = "))
Elec_cost = float(input("Enter Electricity Cost Per Unit = ₹"))
Fridge_cost = float(input("Enter Fridge Rent Cost = ₹"))
person_count = int(input("Enter Total Living Persons In Flat = "))

# ----- TAKE PERSON NAMES FIRST -----
persons = []

print("\nEnter Person Names (Who Will Pay):")
for i in range(person_count):
    name = input(f"Enter Name of Person {i+1}: ")
    persons.append(name)

# ----- CALCULATIONS -----
Electricity_bill = Elect_Unit * Elec_cost

Rent_per_person = Rent / person_count
Food_per_person = Food / person_count
Electricity_per_person = Electricity_bill / person_count
Fridge_per_person = Fridge_cost / person_count

Total_per_person = round(
    Rent_per_person +
    Food_per_person +
    Electricity_per_person +
    Fridge_per_person, 2
)

# ----- INDIVIDUAL PAYMENT STATEMENTS -----
print("\n========== INDIVIDUAL PAYMENT DETAILS ==========\n")

for person in persons:
    print(f"💳 Payment Statement for {person}")
    print(f"{person} needs to pay ₹{Total_per_person:.2f}")
    print(f"➡️ Pay To: Flat Owner / Common Flat Account")
    print("-" * 55)

# ----- DETAILED BREAKDOWN (OPTIONAL BUT USEFUL) -----
print("\n========== PER PERSON BREAKDOWN ==========")
print(f"🏠 Rent        : ₹{Rent_per_person:.2f}")
print(f"🍔 Food        : ₹{Food_per_person:.2f}")
print(f"⚡ Electricity : ₹{Electricity_per_person:.2f}")
print(f"🧊 Fridge      : ₹{Fridge_per_person:.2f}")

# ----- SUMMARY -----
print("\n========== MONTHLY SUMMARY ==========")
print(f"Total Members            : {person_count}")
print(f"Total Electricity Bill   : ₹{Electricity_bill:.2f}")
print(f"Each Person Final Amount : ₹{Total_per_person:.2f}")

# ----- ELECTRICITY INSIGHT -----
print("\n========== ELECTRICITY USAGE INSIGHT ==========")

if Electricity_bill > 600:
    print("⚠️ HIGH electricity usage detected.")
elif Electricity_bill > 400:
    print("⚠️ Average usage detected.")
elif Electricity_bill >= 250:
    print("✅ Good electricity usage.")
else:
    print("🌱 Excellent low electricity usage.")

print("\n========== PAYMENT SETTLEMENT COMPLETE ==========\n")
