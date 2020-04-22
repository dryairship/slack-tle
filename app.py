import os
import logging
import ssl
import certifi
from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter
from bot_messages import handle_command, handle_invalid_channel

app = Flask(__name__)
slack_events_adapter = SlackEventAdapter(os.environ['SLACK_SIGNING_SECRET'], "/slack/events", app)
slack_web_client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])
bot_user_id = None
bot_id = None
bot_username = None

def channel_is_valid(channel_id):
    info = slack_web_client.conversations_info(channel=channel_id)
    return 'is_private' in info['channel'] and not info['channel']['is_private']

@slack_events_adapter.on("app_mention")
def app_mention(payload):
    event = payload.get("event", {})

    channel_id = event.get("channel")
    user_id = event.get("user")
    text = event.get("text")

    message = handle_invalid_channel()
    if channel_is_valid(channel_id):
        message = handle_command(user_id, text)

    response = slack_web_client.chat_postMessage(channel=channel_id, text=message)


if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())

    ssl_context = ssl.create_default_context(cafile=certifi.where())

    client_data = slack_web_client.auth_test()
    bot_user_id = client_data['user_id']
    bot_id = client_data['bot_id']
    bot_username = client_data['user']

    app.run(port=3000)