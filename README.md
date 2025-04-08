# My Crypto Alerts Bot 🤩
## ☕️  Project Context
**Cryptalme** is a simple Python bot written for your crypto Alert needs. The main point of this project is for providing crypto price alerts using a public API.
We'll use the the CoinGecko API, which doesn't require an API key and is free to use.


## ✅  Features
* Checks the price of a specified cryptocurrency (like BTC, ETH).
* Sends an alert (in this case, prints to console or sends via email/notification if extended) when a threshold is crossed.
* Lightweight and easy to run on a schedule (via cron or loop).


## 🛠️  Technical Requirements
* Install python 3.7+
* Install ***requests*** libraries : *pip install requests*


## ▶️  Execution
* Download ***cryptalme.py*** file.
* Open a terminal and run the file as follows:
  * *python cryptalme.py* 
* As a result explaination, it will:
  * Monitor the price of Bitcoin (or the coin you configure)
  * Alert in the console when the price hits or exceeds your set threshold.

 
## 🔄  Customization
* Change Bitcoin crypto to another one: Set CRYPTO_ID = 'ethereum' or any valid CoinGecko coin ID.
* Set different threshold: Change PRICE_THRESHOLD to your desired alert level.
* Change interval: Modify CHECK_INTERVAL for faster or slower checks.


## ⚙️  Technologies Used
* Python ->	Main programming language
* requests ->	HTTP client for API calls
* CoinGecko API	-> Public crypto price API (no key needed)
