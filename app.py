import os
import logging
import ssl
import certifi
import time
from flask import Flask, send_from_directory
from slack import WebClient
from slackeventsapi import SlackEventAdapter
from bot_messages import BotMessagesManager
import asyncio
import util.codeforces_api as cf

app = Flask(__name__)
slack_events_adapter = SlackEventAdapter(os.environ['SLACK_SIGNING_SECRET'], "/slack/events", app)
slack_web_client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])

bot_user_id = None
bot_id = None
bot_username = None
bot_message_manager = None

event_loop = None

def channel_is_valid(channel_id):
    info = slack_web_client.conversations_info(channel=channel_id)
    return 'is_private' in info['channel'] and not info['channel']['is_private']

@slack_events_adapter.on("app_mention")
def app_mention(payload):
    event = payload.get("event", {})
    channel_id = event.get("channel")
    user_id = event.get("user")
    text = event.get("text")

    event_ts = float(event.get("ts"))
    current_ts = time.time()
    time_difference = current_ts-event_ts
    if time_difference > 5:
        return

    message = bot_message_manager.handle_invalid_channel()
    if channel_is_valid(channel_id):
        message = bot_message_manager.handle_command(bot_user_id, user_id, text)

    response = slack_web_client.chat_postMessage(channel=channel_id, blocks=message)

@app.route('/data/<path:path>')
def send_js(path):
    return send_from_directory('data/temp', path)

if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())

    ssl_context = ssl.create_default_context(cafile=certifi.where())

    client_data = slack_web_client.auth_test()
    bot_user_id = client_data['user_id']
    bot_id = client_data['bot_id']
    bot_username = client_data['user']

    event_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(event_loop)
    event_loop.run_until_complete(cf.initialize())
    bot_message_manager = BotMessagesManager(event_loop)

    app.run(port=3000)