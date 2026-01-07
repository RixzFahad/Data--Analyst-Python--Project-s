# Input We Need To Take From User's
"""Cost OF Room Rent"""
"""Total Food Spend For Snacking"""
"""Electricity Unit Spend A Month"""
"""Cost of Per/Unit Of Electricity"""
"""Total Living Person's In Flat"""
""" Rental Fridge Cost"""
#Total Amount You Have To Pay Is--- Result


Rent = int(input("Enter Your Flat Rent = "))
Food = float(input("Enter Total Food Expenses = "))
Elect_Unit = float(input("Enter Electricity Unit spend = "))
Elec_cost = float(input("Enter Electricity cost per unit = "))
Fridge_cost = int(input("Enter The Cost Of Fridge Rent = "))
person = int(input("Enter Total Living Person's In Flat = "))



Rent_per_person = Rent/person
print("Per/Person Need To Pay:", Rent_per_person)

Food_per_person = Food/person
print("Total Food Expenses:", Food_per_person)
Elect_unit_per_person = Elect_Unit*Elec_cost/person
print("Total Electricity Cost per Person:", Elect_unit_per_person)
fridge_cost_per_person = Fridge_cost/person
print("Total Fridge Cost per Person:", fridge_cost_per_person)


Final_to_pay = Rent_per_person + Food_per_person + Elect_unit_per_person + fridge_cost_per_person
print("Everyone Need To Pay :", Final_to_pay)


Electricity_bill = Elect_Unit*Elec_cost
print("The Bill For Electricity Is :", Electricity_bill)

# Electricity Usage Analysis
if Electricity_bill > 600:
    print("⚠️ Bill is HIGH! Reduce electricity usage.")
elif Electricity_bill > 400:
    print("⚠️ Bill is AVERAGE. Use electricity wisely.")
elif Electricity_bill >= 250:
    print("✅ Good usage. Keep it low.")
else:
    print("🌱 Excellent! Very low electricity usage.")