import telebot
import os
import re
import json
import requests
from string import Template

BOT_TOKEN = os.getenv("BOT_TOKEN", None)
API_TOKEN = os.getenv("API_TOKEN", None)
API_URL = os.getenv("API_URL", None)

if BOT_TOKEN is None or API_TOKEN is None or API_URL is None:
    exit("Missing environment variables")

bot = telebot.TeleBot(BOT_TOKEN)

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "X-API-KEY": API_TOKEN
}

template = Template("""
        query {
            record(name: "$ens") {
                owner
            }
        }
        """)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing? Ask for an /ens and I'll tell you if it's available.")

@bot.message_handler(commands=['ens'])
def check_ens(message):
    ens = message.text.split()[1]
    print(f"Checking {ens}")
    if not bool(re.match('^[a-zA-Z0-9]+$', ens)):
        bot.reply_to(message, "Invalid ENS. Use alphanumeric characters.")
        print("Invalid ENS")
        return
    query = template.substitute(ens=ens)
    response = requests.post(API_URL, json={'query': query}, headers=headers)
    if response.status_code != 200:
        print("Error from zettablock", response.status_code)
        bot.reply_to(message, "We've an error. Try later.")
        return
    d = json.loads(response.text)['data']['record']
    print(f"Available {d['owner']}")
    m = "Available!" if d['owner'] is None else f"Owned by {d['owner']}"
    bot.reply_to(message, m)

bot.infinity_polling()