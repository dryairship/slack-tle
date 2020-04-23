import json

import util.codeforces_api as cf
import util.graphs as graphs

class BotMessagesManager:
    def __init__(self, event_loop):
        self.event_loop = event_loop

    def get_blocks_for_text_message(self, message):
        return [{
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": message,
            }
        }]

    def get_blocks_for_image_file(self, filepath):
        return [{
            "type": "image",
            "image_url": filepath,
            "alt_text": "Image"
        }]

    def handle_invalid_channel(self):
        return self.get_blocks_for_text_message("The bot is currently disabled in private channels and DMs.")

    def handle_help(self):
        return self.get_blocks_for_text_message(
            '''
            Hi! The following commands are supported as of now:
                `help`
                `fetch`
                `rating`
            '''
        )

    def handle_fetch_user(self, user):
        result = self.event_loop.run_until_complete(cf.user.info(handles=[user]))
        return self.get_blocks_for_text_message(json.dumps(result))

    def handle_rating_users(self, users):
        graph_file = self.event_loop.run_until_complete(graphs.get_rating_graph_file(handles=users))
        return self.get_blocks_for_image_file(graph_file)

    def handle_command(self, bot_user_id, user_id, text):
        parts = text.split()

        if not bot_user_id in parts[0]:
            return self.get_blocks_for_text_message("I'm a busy bot. Call me only when you need me. :angry:")

        if parts[1] == "help":
            return self.handle_help()
        if parts[1] == "fetch":
            return self.handle_fetch_user(parts[2])
        if parts[1] == "rating":
            return self.handle_rating_users(parts[2:])

        return self.handle_help()