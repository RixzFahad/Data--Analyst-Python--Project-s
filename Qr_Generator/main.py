# Import segno library
# Segno is used to generate QR codes
import segno

# Step 1: Take UPI ID input from the user
# Example: rixz0069@ibl
upi_id = input("Enter User Upi ID: ")

# Step 2: Create the UPI payment URL
# This URL follows the standard UPI payment format
# pa = Payee Address (UPI ID)
# pn = Payee Name
# am = Amount
# cu = Currency (INR)
# tn = Transaction Note
upi_url = (
    f"upi://pay?"          # UPI payment protocol
    f"pa={upi_id}&"        # Payee UPI ID
    f"pn=RecipientName&"   # Receiver name
    f"am=10&"              # Amount to be paid
    f"cu=INR&"             # Currency (Indian Rupee)
    f"tn=UPI_Payment"      # Transaction note
)

# Step 3: Generate QR code from the UPI URL
# segno.make() creates a QR code object
qr = segno.make(upi_url)

# Step 4: Save the generated QR code as an image file
# scale controls the size of the QR code
# higher scale = bigger image
qr.save(
    "upi_payment_qr.png",  # File name
    scale=10               # Size of the QR code
)

# Step 5: Success message
print("QR Generated Successfully ✅")
