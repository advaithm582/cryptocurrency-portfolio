# This file is part of Cryptocurrency Portfolio.

# Cryptocurrency Portfolio is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Cryptocurrency Portfolio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Cryptocurrency Portfolio.  If not, see <https://www.gnu.org/licenses/>.


import requests
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from cryptocurrency_portfolio.models import CryptocoinPortfolio
from cryptocurrency_portfolio.constants import DB_URL


class InvalidCurrencyException(Exception):
	def __init__(self):
		self.msg = "Invalid Currency"

class CryptoAPIException(Exception):
	def __init__(self, msg):
		self.__error_code = {}
		self.msg = msg

# Functions

class CryptoPortfolio():
	__CURRENCY_SYMBOLS = {"INR":"₹", "USD":"$", "GBP":"£", "EUR":"€"}
	__api_request_performed = False
	__api_request_data = {}
	def __init__(self, portfolio, api_key, api_domain = "https://pro-api.coinmarketcap.com", currency_code = "USD"):
		self.__portfolio = portfolio
		self.__api_key = api_key
		self.__api_domain = api_domain
		self.__currency_code = currency_code

	def update_portfolio(self, new_portfolio):
		"""Update portfolio"""
		del self.__portfolio
		self.__portfolio = new_portfolio

	def get_symbol(self):
		if self.__currency_code in self.__CURRENCY_SYMBOLS:
			return self.__CURRENCY_SYMBOLS[self.__currency_code]
		else:
			raise InvalidCurrencyException()

	def is_profit(self, num):
		if num >= 0:
			return True
		else:
			return False

	def __call_api(self, force_update = False):
		if not self.__api_request_performed or force_update:
			custom_headers = {"X-CMC_PRO_API_KEY" : self.__api_key} # Custom HTTP header for API auth
			api_url = self.__api_domain + "/v1/cryptocurrency/listings/latest?start=1&limit=30&convert=" + self.__currency_code #URL
			api_request = requests.get(api_url, headers=custom_headers)
			self.__api_request_data = json.loads(api_request.content)
			self.__api_request_performed = True

		return self.__api_request_data

	def force_api_update_and_get_portfolio(self):
		"""Forces an update to the API data and gets the portfolio"""
		self.__api_request_data = ""
		self.__call_api(True)
		return self.get_portfolio()

	def get_portfolio(self):
		f_response = []

		# currency_sym = self.get_symbol(CURRENCY_CODE)
		inv_coins = self.__portfolio
		# custom_headers = {"X-CMC_PRO_API_KEY" : COINMARKETCAP_API_KEY} # Custom HTTP header for API auth
		# api_url = API_DOMAIN + "/v1/cryptocurrency/listings/latest?start=1&limit=20&convert=USD" #URL
		# api_request = requests.get(api_url, headers=custom_headers) # HTTP GET

		# Format in JSON
		api_result = self.__call_api()

		# Total Profit or Loss
		total_p_or_l = 0

		for result in api_result["data"]:
			# For loop
			for coin in inv_coins:
				if result["symbol"] == coin["symbol"]:
					# Total paid at time of purchase
					total_paid = coin["num_owned"] * coin["price_per_coin"]
					# Current value
					current_value = coin["num_owned"] * result["quote"][self.__currency_code]["price"]
					# Profit or loss per coin:
					p_or_l_per_coin = result["quote"][self.__currency_code]["price"] - coin["price_per_coin"]
					# Overall profit or loss:
					overall_p_or_l = p_or_l_per_coin * coin["num_owned"]

					# Add to aggregate
					total_p_or_l += overall_p_or_l
					# print("Currency: %s (%s)" % (result["name"], result["symbol"]))
					# print("Price: %.2f USD" % result["quote"]["USD"]["price"])
					# print("Number of Coins Owned: %d" % (coin["num_owned"]))
					# print("Amount Paid at time of purchase: %s%.2f" % (currency_sym, total_paid))
					# print("Current market value of all your coins: %s%.2f" % (currency_sym, current_value))
					# # Profit or Loss per coin:
					# print("%s per coin: %s%.2f" % (get_profit_or_loss(p_or_l_per_coin), currency_sym, abs(p_or_l_per_coin)))
					# print("%s for all your coins: %s%.2f" % (get_profit_or_loss(overall_p_or_l), currency_sym, abs(overall_p_or_l)))
					# print("-------------------------------")
					coin_data = {
						"id" : coin["id"],
						"name" : result["name"],
						"symbol" : result["symbol"],
						"price": round(result["quote"][self.__currency_code]["price"], 2),
						"num_coins_owned" : coin["num_owned"],
						"amount_paid" : round(total_paid, 2),
						"current_market_value" : round(current_value, 2),
						"pl_per_coin" : round(p_or_l_per_coin, 2),
						"pl_all_coins" : round(overall_p_or_l, 2)
					}
					f_response.append(coin_data)
		return f_response
		# print("\n%s for all your coins of all currencies: %s%.2f" % (get_profit_or_loss(total_p_or_l), currency_sym, abs(total_p_or_l)))

	def get_total_pl(self):
		"""Get total profit or loss for all coins"""

		inv_coins = self.__portfolio
		api_result = self.__call_api()
		total_p_or_l = 0

		for result in api_result["data"]:
			# For loop
			for coin in inv_coins:
				if result["symbol"] == coin["symbol"]:
					# Total paid at time of purchase
					# total_paid = coin["num_owned"] * coin["price_per_coin"]
					# Current value
					# current_value = coin["num_owned"] * result["quote"][self.__currency_code]["price"]
					# Profit or loss per coin:
					p_or_l_per_coin = result["quote"][self.__currency_code]["price"] - coin["price_per_coin"]
					# Overall profit or loss:
					overall_p_or_l = p_or_l_per_coin * coin["num_owned"]

					# Add to aggregate
					total_p_or_l += overall_p_or_l

		return total_p_or_l

	def get_total_current_value(self):
		"""Get total profit or loss for all coins"""

		inv_coins = self.__portfolio
		api_result = self.__call_api()
		total_currval = 0

		for result in api_result["data"]:
			# For loop
			for coin in inv_coins:
				if result["symbol"] == coin["symbol"]:
					# Total paid at time of purchase
					# total_paid = coin["num_owned"] * coin["price_per_coin"]
					# Current value
					current_value = coin["num_owned"] * result["quote"][self.__currency_code]["price"]
					# Profit or loss per coin:
					# p_or_l_per_coin = result["quote"][self.__currency_code]["price"] - coin["price_per_coin"]
					# Overall profit or loss:
					# overall_p_or_l = p_or_l_per_coin * coin["num_owned"]

					# Add to aggregate
					total_currval += current_value

		return total_currval

	def get_total_paid_amount(self):
		"""Get total amount paid by user"""

		inv_coins = self.__portfolio
		api_result = self.__call_api()
		total_paid = 0

		for result in api_result["data"]:
			# For loop
			for coin in inv_coins:
				if result["symbol"] == coin["symbol"]:
					# Total paid at time of purchase
					total_paid_for_that_coin = coin["num_owned"] * coin["price_per_coin"]
					# Current value
					# current_value = coin["num_owned"] * result["quote"][self.__currency_code]["price"]
					# Profit or loss per coin:
					# p_or_l_per_coin = result["quote"][self.__currency_code]["price"] - coin["price_per_coin"]
					# Overall profit or loss:
					# overall_p_or_l = p_or_l_per_coin * coin["num_owned"]

					# Add to aggregate
					total_paid += total_paid_for_that_coin

		return total_paid


class DatabaseHandler():
	def __init__(self):
		engine = create_engine(DB_URL)
		Session = sessionmaker(bind=engine)
		self.__db_session = Session()

	def add_coin(self, symbol, num_owned, price_per_coin, auto_commit = True):
		"""Adds a coin to the portfolio"""
		coin = CryptocoinPortfolio(symbol=symbol, num_owned=num_owned, price_per_coin=price_per_coin)
		self.__db_session.add(coin)
		if auto_commit:
			self.commit_changes()

	def delete_coin(self, coin_id, auto_commit = True):
		"""Deletes a coin from the portfolio"""
		to_delete = self.__db_session.query(CryptocoinPortfolio).filter_by(id=coin_id).one()
		self.__db_session.delete(to_delete)
		if auto_commit:
			self.commit_changes()

	def update_coin(self, coin_id, symbol, num_owned, price_per_coin, auto_commit = True):
		"""Updates the coin data in the database"""
		to_update = self.__db_session.query(CryptocoinPortfolio).filter_by(id=coin_id).one()
		(to_update.symbol, to_update.num_owned, to_update.price_per_coin) = (symbol, num_owned, price_per_coin)
		if auto_commit:
			self.commit_changes()

	def get_coin_data_to_list(self):
		"""Queries coin data from SQL database and outputs it as a list cum dict"""
		output_list = [] # Output list
		query = self.__db_session.query(CryptocoinPortfolio).order_by(CryptocoinPortfolio.symbol)
		for record in query:
			portfolio_data = {
				"id" : record.id,
				"symbol" : record.symbol, # Symbol
				"num_owned" : record.num_owned, # No. of coin owned
				"price_per_coin" : record.price_per_coin # Price per coin at time of purchase
			}
			output_list.append(portfolio_data)
		return output_list

	def truncate_table(self, auto_commit = True):
		"""Remove all coins"""
		self.__db_session.query(CryptocoinPortfolio).delete()
		if auto_commit:
			self.commit_changes()


	def commit_changes(self):
		"""Make changes reflect in database"""
		self.__db_session.commit()

