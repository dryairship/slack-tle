import os
import logging
from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter
import ssl as ssl_lib
import certifi


app = Flask(__name__)
slack_events_adapter = SlackEventAdapter(os.environ['SLACK_SIGNING_SECRET'], "/slack/events", app)
slack_web_client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])
bot_user_id = None
bot_id = None
bot_username = None

@slack_events_adapter.on("message")
def message(payload):
    event = payload.get("event", {})

    channel_id = event.get("channel")
    user_id = event.get("user")
    text = event.get("text")

    if user_id == bot_user_id:
        return

    message = "Hey! As of now, I only understand meows. So if you meow to me I'll meow back."
    if text and text.lower() == "meow":
        message = "Meeoowwwww!!!"
    response = slack_web_client.chat_postMessage(channel=channel_id, text=message)

if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())

    ssl_context = ssl_lib.create_default_context(cafile=certifi.where())

    client_data = slack_web_client.auth_test()
    bot_user_id = client_data['user_id']
    bot_id = client_data['bot_id']
    bot_username = client_data['user']

    app.run(port=3000)