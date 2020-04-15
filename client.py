import Adyen
import sys, webbrowser
from ady_paymentMethods import ady_paymentMethods
from input_checks import input_number, input_string
from secrets import secrets

# Introduction
print("\nTEST - Thank you for taking the time to donate!\n")

# Get all payments methods for the account
print("Please input your country, like:\nNL - Netherlands\nAT - Austria\nUS - USA")
country = input_string("\nPlease input your country code (2 letters): ", 2, 2)
if country == "NL" or "AT":
    currency = "EUR"
elif country == "US":
    currency = "USD"
else:
    # Considering EUR as the default currency
    currency = "EUR"
payment_method = ady_paymentMethods(country, currency)

# Display for preferred payment method
print("\n\nWhat is your preferred payment method? ")
i = 0
for method in payment_method.message['paymentMethods']:
    i += 1
    print(str(i) + '. ' + method['name'])

# Manage input
stay_in_loop = True
while stay_in_loop:
    try:
        preferred_payment_method = input_number("Please input your choice: ", 1, 2)
        preferred_payment_method = int(preferred_payment_method)-1
        # No need to convert the index ID to the proper name
        # preferred_payment_method = payment_method.message['paymentMethods'][preferred_payment_method]['name']
        stay_in_loop = False
    except IndexError:
        print("Your choice is not in the list, please retry.")

# convert preferred_payment_method for readability
preferred_payment_method = payment_method.message['paymentMethods'][preferred_payment_method]

if preferred_payment_method['type'] == "scheme": # Credit Card
    # Get Scheme info and build the dataset
    print("\nWe'll collect now your card details:")
    client_paymentMethod = {'holderName': input("Enter your name: "),
                            'type': "scheme",
                            'number': input_number("Enter your card number: ", 16, 16),
                            'expiryMonth': input_number("Enter your card expiry month: ", 2, 2),
                            'expiryYear': input_number("Enter your card expiry year: ", 4, 4),
                            'cvc': input_number("Enter your card security code: ", 3, 4)}

elif preferred_payment_method['type'] == "ideal":
    # Ask for iDeal bank
    print("\n\nWhat is your iDeal bank? ")
    i = 0
    for bank in preferred_payment_method['details'][0]['items']:
        i += 1
        print(str(i) + '. ' + bank['name'])

    # Manage input
    stay_in_loop = True
    while stay_in_loop:
        try:
            ideal_bank = input_number("Please input your choice: ", 1, 2)
            ideal_bank = int(ideal_bank) - 1
            ideal_bank = preferred_payment_method['details'][0]['items'][ideal_bank]['id']
            stay_in_loop = False
        except IndexError:
            print("Your choice is not in the list, please retry.")

    # Build the dataset
    client_paymentMethod = {'type': "ideal",
                            'issuer': ideal_bank}

elif preferred_payment_method['type'] == "directEbanking": # Sofort
    client_paymentMethod = {
                               'type': "directEbanking",
                           }

else:
    print("\nThe payment method \"" + preferred_payment_method['name'] + "\" isn't supported by this script. Exiting...")
    sys.exit()

# Secrets are retrieved
secret = secrets()

# Adyen API configuration
ady = Adyen.Adyen()
ady.client.xapikey = secret['xapikey']
ady.payment.client.app_name = secret['app_name']

# Adyen API call
payment_result = ady.checkout.payments(
    {
        "amount": {
            "currency": currency,
            "value": 1000,
        },
        "reference": "ORDER ID",
        "paymentMethod": client_paymentMethod,
        'returnUrl': 'https://0.0.0.0',
        "merchantAccount": secret['merchantAccount']
    }
)

# Result must be parsed and presented to the user
if payment_result.message['resultCode'] == "RedirectShopper":
    webbrowser.open(payment_result.message['action']['url'], new=2)
else:
    print(payment_result.message['resultCode'])

# If require additional action (like Sofort), the redirect could be handled with a browser start. But this would require also to handle back the response.