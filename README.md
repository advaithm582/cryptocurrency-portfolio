# Cryptocurrency Portfolio
This software uses the CoinMarketCap API to calculate your profits and losses. To use the same you need a CoinMarketCap Pro API key, which can be procured from [the CMC Pro API registration page](https://pro.coinmarketcap.com/signup/ "CMC Pro API registeration page"). You can choose any plan that suits you.

## Compiling the app for your operating system
This is required in order to add your API key to the app.

>**Note:** On Windows, use the inbuilt DB manipulation tool to modify the DB instead of compiling the program, if you don't know Python.

Compiling the app requires:
* pip
* python >=3.8
Python packages:
* pyinstaller >= 4.3 (to compile into executable)
* requests >= 2.25.1
* sqlalchemy >= 1.4.17

Steps to compile the app:
1. Open Terminal
2. Ensure you are in the directory of the source code. If not, use the `cd` command to do so.
3. Change directory using `cd cryptocurrency_portfolio`
4. Type `pyinstaller views.py --onefile --noconsole -i=Bitcoin-BTC-icon.ico`

## Constants in `config.json`
Key | Value
----|------
COINMARKETCAP_API_KEY | The CoinMarketCap API key, get one here: https://pro.coinmarketcap.com/
API_DOMAIN | API Domain, https://pro-api.coinmarketcap.com for paid API, https://api.coinmarketcap.com may not work with this app
CURRENCY_CODE | The code for your currency e.g INR, USD, GBP etc. Note: This app does not support all currency codes, see line 21 in `controllers.py`
DB_URL | The SQLAlchemy DB URI to be used. Leave it as it is
THEME_FILE | For future use, it is ignored currently.

## Application Architecture
![Application Architecture](https://lh6.googleusercontent.com/jurmX35WHNBmAuP0fzeComLLC3VW_iv-VeRF7nGbO0W-cmUJsi5403TrFakXLIu6VqrTx1ubVgtXDdo-lXbI=w1673-h937-rw)

## Screenshots
![Screenshot](https://lh5.googleusercontent.com/9VHUizUF1NTyhZUv99DguNOqW55PWpMssbdQ-ON40md0kLMTx-1BD2THNWIoUN4Yv3qD4EQiaeMSGlwLwbaE=w1673-h969-rw)