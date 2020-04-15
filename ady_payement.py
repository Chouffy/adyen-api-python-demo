from secrets import secrets


def ady_payment_scheme(**kwargs):
    # Arguments needed:
    #  - currency in minor unit - https://docs.adyen.com/development-resources/currency-codes
    #  - amount in int
    #  - reference


    # Import all secrets
    secret = secrets()

    payment_info = {
        "amount": {
            "currency": "USD",
            "value": 1000,
        },
        "reference": kwargs['reference'],
        "paymentMethod": {
            "type": "scheme",
            "number": "4111111111111111",
            "expiryMonth": "10",
            "expiryYear": "2020",
            "cvc": "737",
            "holderName": "S.Hopper"
        },
        "returnUrl": "https://your-company.com/..",
        "merchantAccount": secret['merchantAccount']
    }
