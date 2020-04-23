import util.codeforces_api as cf
import json
import asyncio

class BotMessagesManager:
    def __init__(self, event_loop):
        self.event_loop = event_loop

    def handle_invalid_channel(self):
        return "The bot is currently disabled in private channels and DMs."

    def handle_help(self):
        return '''
        Hi! The following commands are supported as of now:
        `help`
        `fetch`
        `rating`
        '''

    def handle_fetch_user(self, user):
        result = self.event_loop.run_until_complete(cf.user.info(handles=[user]))
        return json.dumps(result)

    def handle_rating_user(self, user):
        result = self.event_loop.run_until_complete(cf.user.rating(handle=user))
        return json.dumps(result)

    def handle_command(self, bot_user_id, user_id, text):
        parts = text.split()

        if not bot_user_id in parts[0]:
            return "I'm a busy bot. Call me only when you need me. :angry:"

        if parts[1] == "help":
            return self.handle_help()
        if parts[1] == "fetch":
            return self.handle_fetch_user(parts[2])
        if parts[1] == "rating":
            return self.handle_rating_user(parts[2])

        return self.handle_help()