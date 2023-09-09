import openach

# Create a new payment gateway
gateway = openach.PaymentGateway()

# Set up the gateway with your OpenACH credentials
gateway.setCredentials('your_openach_username', 'your_openach_api_key')

# Create a new payment profile for a customer
profile = gateway.createProfile('customer_id', 'customer_name', 'customer_email')

# Add a bank account to the customer's profile
account = gateway.addBankAccount(profile, 'account_number', 'routing_number', 'account_type')

# Charge the customer
transaction = gateway.charge(account, 100.00)  # Charge $100.00

# Check if the transaction was successful
if transaction.success:
    print("Payment successful!")
else:
    print("Payment failed: " + transaction.message)
