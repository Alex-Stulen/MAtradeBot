<h1 style="text-align: center;">MA Trade Telegram Bot</h1>
<hr>

## Description:
<p>This bot allows you to get information about crypto pairs. Integrated with the site https://paper-trader.frwd.one/</p>

## Pre-requirements:
* Python 3.6+ (developed and tested on version 3.10.8). Recommended Version: 3.10.8
* Having an <strong>.env</strong> file at the root of the project (See section .ENV Description)

## Requirements:
All project dependencies in the <strong>requirements.txt</strong> file in the project root folder

## .ENV Description:
<p>Description of all fields in the .env file</p>
<p>
File format: Pairs <-key->=<-value->. Be sure to write equal between key and value without spaces
<br>
Pairs are separated by \n (each pair on a new line)
</p>
<strong>BOT_TOKEN</strong> - Telegram bot token (keep secret). Type: string
<br>
<strong>BOT_SKIP_UPDATES</strong> - Skip bot updates or not when starting the bot. Type: bool. Value: True or False
<br>
<strong>MAX_MESSAGE_LEN</strong> - The maximum number of characters for one message. Type: int. Ex: 64
<br>
<strong>USE_POLLING</strong> - Use polling to update the bot or not. Type: bool. Value: True or False. This setting takes precedence over USE_WEBHOOK. If USE_POLLING=True is specified, then the bot will be launched via polling with a 100% chance of ignoring USE_WEBHOOK
<br>
<strong>USE_WEBHOOK</strong> - Use the webhook system to update the bot or not. Type: bool. Value: True or False
<br>
<strong>WEBHOOK_HOST</strong> - Webhook processing host. Specify without a slash at the end. Type: string. Ex: https://example.com
<br>
<strong>WEBHOOK_PATH</strong> - Relative webhook processing path. Put a slash at the beginning. Ex: /api/bot/ma-trade-bot/
<br>
<strong>WEBAPP_HOST</strong> - Host or webhook processing IP. Type: string. Ex: 127.0.0.1
<br>
<strong>WEBAPP_PORT</strong> - Webhook processing port. Type: int. Ex: 8000
<br>

#### Optional .env file options if using USE_POLLING=True:
<p>I recommend that you specify these fields in the .env file, but leave them empty</p>

<strong>WEBHOOK_HOST</strong>
<br>
<strong>WEBHOOK_PATH</strong>
<br>
<strong>WEBAPP_HOST</strong>
<br>
<strong>WEBAPP_PORT</strong>

## .env Example:
<p>
BOT_TOKEN=5886460535:AAGNjT6whBUgvuy5Kgz4hXWshI8jLkQL2PE
<br>
<i>(This is a real token. You can use as an example, up to a certain period :))</i>
<br>  
BOT_SKIP_UPDATES=True
<br>
MAX_MESSAGE_LEN=64
<br>
USE_POLLING=True
<br>
USE_WEBHOOK=False
<br>
WEBHOOK_HOST=
<br>
WEBHOOK_PATH=/
<br>
WEBAPP_HOST=
<br>
WEBAPP_PORT=
</p>

<hr>

## Bot startup:
1. Set up the .env file
2. Create a python virtual environment
3. Install dependencies from requirements.txt file
4. Command to start the bot:
<br>  
<code style="padding: 10px;">python ma_trade_bot/run_bot.py</code>

<hr>

## Author
<p>
    Alex Stulen
    <br>
    Email: <strong>ookno16@gmail.com</strong>
    <br>
    Developed and written in December 2022
</p>

<hr>  

<h3 style="text-align: center;">Agreement</h2>
<p style="text-align: center;">By using this software, you agree that this software is developed for informational purposes ONLY. The author does not take any responsibility for how this software is used, whether this software works or not, whether it solves your problem or not, etc.</p>

<p style="text-align: center;">December 2022</p>