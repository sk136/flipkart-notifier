# Flipkart-Notifier
This Script notifies when the product gets in stock to your pincode on FK

## Why this script?
Generally Flipkart doesn't provide NOTIFY button when the product is not available particularly to your pincode.This script notifies when product gets in stock to your location.This script sends notification to DISCORD Server.

## Install
- Clone the repo `git clone https://github.com/sk136/flipkart-notifier.git`
- Install requirements.txt `pip install -r requirements.txt`

## Configure
- Before running the script you have to setup the script properly
- Enter the pincode
- Enter the URL
- Enter the Refresh FREQUENCY (page refresh rate) (Default 5)
- Enter the message counter(no.of prompts to discord server) (Default 3) 
- Setup discord webhook bot

## Discord Setup
- Signup Discord if you don't have
- Create a server
- Create a webhook and name the bot
- Copy the webhook URL
- Paste in bot.py
- You can use telegram too if you want

## Run the Bot
- Better to Run the script in IDE if you waana run bot on Local Server (to distinguish Driver Shell and Python Shell) 
- If you wanna run bot on cloud slightly change the script based on cloud requirments
