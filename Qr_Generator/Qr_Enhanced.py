# Import segno library
# Segno is used to generate QR codes
import segno
import os

# Step 1: Take UPI ID input from the user
upi_id = input("Enter User UPI ID: ")

# Step 2: Take a custom name for the QR file
# This name will be used to save the QR image
file_name = input("Enter name for QR file (without extension): ")

# Step 3: Create the UPI payment URL
# pa = Payee Address (UPI ID)
# pn = Payee Name
# am = Amount
# cu = Currency (INR)
# tn = Transaction Note
upi_url = (
    f"upi://pay?"
    f"pa={upi_id}&"
    f"pn=RecipientName&"
    f"am=10&"
    f"cu=INR&"
    f"tn=UPI_Payment"
)

# Step 4: Generate QR code from the UPI URL
qr = segno.make(upi_url)

# Step 5: Create full file name with .png extension
final_file_name = f"{file_name}.png"

# Step 6: Save the QR code in the same folder
# Each QR will be saved with a different name
qr.save(
    final_file_name,
    scale=10
)

# Step 7: Success message
print(f"QR Generated Successfully ✅ Saved as '{final_file_name}'")
