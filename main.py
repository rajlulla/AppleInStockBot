from flask import Flask
from threading import Thread
import requests

carrier = "UNLOCKED/US" # Can be "TMOBILE_IPHONE14PRO", "SPRINT_IPHONE14PRO", "ATT_IPHONE14PRO", "VERIZON_IPHONE14PRO"
model = "MQ8R3LL/A" # Insert your model number here, can be found on Best Buy
zip = "#####" # Insert your zip code
botToken = "270485614:AAHfiqksKZ8WmR2zSjiQ7_v4TMAKdiHm9T0" # Get telegram bot token from @BotFather
chatID = "##########" # Get your chat ID by sending a message to your bot and checking https://api.telegram.org/bot{botToken}/getUpdates

app = Flask('')

@app.route('/')
def home():
    url = f"https://www.apple.com/shop/fulfillment-messages?pl=true&mts.0=regular&mts.1=compact&cppart={carrier}&parts.0={model}&location={zip}"

    payload={}
    headers = {
      'authority': 'www.apple.com',
      'accept': '*/*',
      'accept-language': 'en-US,en;q=0.9',
    }
    
    response = requests.request("GET", url, headers=headers, data=payload)
    
    json_resp = response.json()

    print(json_resp)

    text = json_resp["body"]["content"]["pickupMessage"]["stores"][0]["partsAvailability"][model]["pickupSearchQuote"]

    text_url = text.replace(" ", "+")

    requests.request("GET", f"https://api.telegram.org/bot{botToken}/sendMessage?chat_id={chatID}&text={text_url}")

    return text

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

keep_alive()