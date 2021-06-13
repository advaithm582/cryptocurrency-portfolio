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

