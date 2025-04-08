import requests
import time

# CONFIGURATION
CRYPTO_ID = 'bitcoin'  # CoinGecko coin ID, e.g., 'bitcoin', 'ethereum'
CURRENCY = 'usd'
PRICE_THRESHOLD = 70000  # Set your alert threshold
CHECK_INTERVAL = 60  # In seconds

def get_crypto_price(crypto_id, vs_currency):
    url = f'https://api.coingecko.com/api/v3/simple/price'
    params = {
        'ids': crypto_id,
        'vs_currencies': vs_currency
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        price = response.json()[crypto_id][vs_currency]
        return price
    except Exception as e:
        print(f"Error fetching price: {e}")
        return None

def run_alert_bot():
    print(f"🔔 Cryptalme is now monitoring {CRYPTO_ID.upper()} price every {CHECK_INTERVAL}s.")
    while True:
        price = get_crypto_price(CRYPTO_ID, CURRENCY)
        if price:
            print(f"Current price of {CRYPTO_ID.upper()}: ${price}")
            if price >= PRICE_THRESHOLD:
                print(f"🚨 ALERT: {CRYPTO_ID.upper()} has reached ${price}!")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    run_alert_bot()
