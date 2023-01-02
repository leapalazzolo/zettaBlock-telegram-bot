# zettablock-telegram-bot

## Description

This is a telegram bot called @isthatensavailablebot that check if an ENS is available or owned. This uses ZettaBlock to fetch the data from the blockchain.

## Install

`pip install -r requirements.txt`

## Usage

1. Create some environment variables:
  * BOT_TOKEN: this is the secret of your telegram bot
  * API_URL: your ZettaBlock API using ENS indexed by name
  * API_TOKEN: your ZettaBlock API token
1. Start the API   `python app.py`
2. Add your telegram bot and use the commands /start, /help and /ens