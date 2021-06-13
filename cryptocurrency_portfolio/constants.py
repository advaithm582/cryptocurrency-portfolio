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

import json

# # Theme
COLOR_SCHEME = {
	"title" : {
		"fg" : "black",
		"bg" : None,
		"font" : {
			"name" : "Calibri",
			"size" : "20",
			"style" : "bold"
		},
		"padding" : {
			"x" : "5",
			"y" : "5"
		},
		"border" : {
			"width" : None,
			"relief" : None
		}
	},
	"header" : {
		"fg" : "white",
		"bg" : "#142E54",
		"font" : {
			"name" : "Calibri",
			"size" : "12",
			"style" : "bold"
		},
		"padding" : {
			"x" : "5",
			"y" : "5"
		},
		"border" : {
			"width" : 2,
			"relief" : "groove"
		}
	},
	"content" : {
		"fg" : "black",
		"bg" : "white",
		"font" : {
			"name" : "Calibri",
			"size" : "12",
			"style" : ""
		},
		"padding" : {
			"x" : "5",
			"y" : "5"
		},
		"border" : {
			"width" : 2,
			"relief" : "groove"
		}
	},
	"button" : {
		"fg" : "black",
		"bg" : "#cccccc",
		"font" : {
			"name" : "Serif",
			"size" : "10",
			"style" : ""
		},
		"padding" : {
			"x" : "5",
			"y" : "5"
		},
		"border" : {
			"width" : 1,
			"relief" : "solid"
		}
	},
	"entry" : {
		"fg" : "black",
		"bg" : "white",
		"font" : {
			"name" : "Serif",
			"size" : "10",
			"style" : ""
		},
		"border" : {
			"width" : 1,
			"relief" : "solid"
		}
	}
}

with open("config.json", "r") as cfg_file:
	cfg = json.loads(cfg_file.read())
	COINMARKETCAP_API_KEY = cfg["COINMARKETCAP_API_KEY"]
	API_DOMAIN = cfg["API_DOMAIN"]
	CURRENCY_CODE = cfg["CURRENCY_CODE"]
	DB_URL = cfg["DB_URL"]

