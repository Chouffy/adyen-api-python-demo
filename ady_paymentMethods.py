import Adyen
from secrets import secrets


def ady_paymentMethods(country, currency):

    # Import all secrets
    secret = secrets()

    ady = Adyen.Adyen()
    client = ady.client
    client.xapikey = secret['xapikey']
    client.platform = secret['platform']
    client.app_name = secret['app_name']

    request = {
        'merchantAccount': secret['merchantAccount'],
        'countryCode': country,
        'amount': {
            'value': 100,
            'currency': currency,
        },
        'channel': 'Web'
    }

    response = ady.checkout.payment_methods(request)
    return response
