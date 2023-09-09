import openach
import os

# Create a new payment gateway
gateway = openach.PaymentGateway()

# Set up the gateway with your OpenACH credentials
# Use environment variables for security
username = os.getenv('OPENACH_USERNAME')
api_key = os.getenv('OPENACH_API_KEY')
if not username or not api_key:
    raise ValueError("Missing OpenACH credentials")

gateway.setCredentials(username, api_key)

# Create a new payment profile for a customer
# Use try/except for error handling
try:
    profile = gateway.createProfile('customer_id', 'customer_name', 'customer_email')
except Exception as e:
    print(f"Failed to create profile: {e}")
    raise

# Add a bank account to the customer's profile
try:
    account = gateway.addBankAccount(profile, 'account_number', 'routing_number', 'account_type')
except Exception as e:
    print(f"Failed to add bank account: {e}")
    raise

# Charge the customer
try:
    transaction = gateway.charge(account, 100.00)  # Charge $100.00
except Exception as e:
    print(f"Failed to charge account: {e}")
    raise

# Check if the transaction was successful
if transaction.success:
    print("Payment successful!")
else:
    print("Payment failed: " + transaction.message)
