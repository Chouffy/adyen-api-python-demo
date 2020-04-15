# Adyen API Integration in Python - Demo

This repo contain a rough implementation of the [Adyen API](https://docs.adyen.com/checkout/api-only) in Python.
The goal was to make a simple payment module to be used for donation or licensing purpose.

API-only integration require authorization from Adyen Sales Support. As such, this code will not succeed when `/payments` is called and will throw `AdyenAPIInvalidPermission` error.    
Also, full PCI compliance is expected as this code collect raw credit card data. I doubt this primitive code is compliant.

The integration isn't finished as payment details and payment result parsing and display are not implemented.


## Requirements
* Python 3.8
* Packages: Adyen, requests
* Adyen account, that you can [request it here](https://www.adyen.com/home/discover/test-account-signup#form).

## Installation
All merchant-specific info are needs to be registered in `secrets.py`. A template is provided: `secrets_template.py`.

1. Install required packages: `pip install Adyen requests`
1. Rename `secrets_template.py` to `secrets.py`.
1. Replace all content with your informations.

## Usage

Run `client.py`

## License
The Unlicense - see LICENSE