package slackbot

import (
	"github.com/slack-go/slack/slackevents"
)

func handleHelp(event *slackevents.AppMentionEvent) {
	SlackBot.PostMessage(event.Channel, messageHelp())
}