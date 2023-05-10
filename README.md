# credit-card-validator
Application for validating credit cards quickly and efficiently.

## Requirements
- Python v3.6+ (with Pip)  
If python3 is not installed on your PC [Click here to download and install it](https://www.python.org/downloads/)

## Installation / Running
This application can be installed in two ways:
- Automatically using the setup script (only tested on linux ubuntu but should work for other flavours or PC with bash terminal)
- Manually

### Automatic Setup
- Clone project to your local computer
![git clone project](https://github.com/austitech/credit-card-validator/assets/53453398/7424d55e-530d-4806-9e86-e4a6000ab18e)
- Change into project directory
![change directory](https://github.com/austitech/credit-card-validator/assets/53453398/ee6aca37-511b-4850-b883-91425c18da86)
- Run project setup script **setup_backend.sh**; The script will create project virtual environment, install dependencies and start the development server.  
![run setup script](https://github.com/austitech/credit-card-validator/assets/53453398/2182071a-7e84-4adc-85d5-735f67842048) 
- You'll know it is done when you see this:  
![Server started](https://github.com/austitech/credit-card-validator/assets/53453398/33144467-50b1-435a-9b65-e08eda8a93ac)
- Open **http://127.0.0.1:7001/docs** on your browser to view the api documentation
- Open **http://127.0.0.1:7001/app** on your browser to view the application

### Manual Setup
- Clone project to your local computer
![git clone project](https://github.com/austitech/credit-card-validator/assets/53453398/7424d55e-530d-4806-9e86-e4a6000ab18e)
- Change into project directory
![change directory](https://github.com/austitech/credit-card-validator/assets/53453398/ee6aca37-511b-4850-b883-91425c18da86)
- Create project virtual environment
![create virtualenv](https://github.com/austitech/credit-card-validator/assets/53453398/a2558ee5-4535-4602-b604-b869c7d8ca18)
- Activate virtual environment
![activate virtualenv](https://github.com/austitech/credit-card-validator/assets/53453398/5c83278e-fa8c-4900-b93a-3626a46713ab)
- Install project requirements
![install requirements](https://github.com/austitech/credit-card-validator/assets/53453398/4ba51160-2523-466f-b893-6e35e9ab48b4)
- Run development server
![Run development server](https://github.com/austitech/credit-card-validator/assets/53453398/db2654bb-f301-4aa8-93db-a9b56363b3a2)
- You will know the server has started when you see this:
![server running](https://github.com/austitech/credit-card-validator/assets/53453398/e9c4e35a-60c2-46d2-8652-8feced384d39)
- Open **http://127.0.0.1:7001/docs** on your browser to view the api documentation
- Open **http://127.0.0.1:7001/app** on your browser to view the application

## Validation Criteria for credit cards
- The expiry date of the credit card must be AFTER present time.
- The CVV (security code) of the credit card must be exactly 3 digits long
  - Unless it’s an American Express card, in which case the CVV must be exactly 4 digits long
  - American Express are cards whose PAN (card numbers) starts with either “34” or “37”
- Card number (PAN) must be between 16 and 19 inclusive.
- Last digit of the PAN (card number) must be valid on check using Luhn’s algorithm.
