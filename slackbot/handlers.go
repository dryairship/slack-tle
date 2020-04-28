package slackbot

import (
	"github.com/slack-go/slack/slackevents"

	"github.com/dryairship/slack-tle/grpc_client"
)

func handleHelp(event *slackevents.AppMentionEvent) {
	SlackBot.PostMessage(event.Channel, messageHelp())
}

func handleRating(event *slackevents.AppMentionEvent, handles []string) {
	if len(handles) == 0 {
		SlackBot.PostMessage(event.Channel, messageHelpRating())
		return
	}

	file, err := grpc_client.HandleRating(handles)
	if err != nil {
		SlackBot.PostMessage(event.Channel, messageError())
		return
	}
	SlackBot.PostMessage(event.Channel, messageRating(file))
}