package slackbot

import (
	"strings"

	"github.com/slack-go/slack/slackevents"
)

/*
type AppMentionEvent struct {
    Type            string      `json:"type"`
    User            string      `json:"user"`
    Text            string      `json:"text"`
    TimeStamp       string      `json:"ts"`
    ThreadTimeStamp string      `json:"thread_ts"`
    Channel         string      `json:"channel"`
    EventTimeStamp  json.Number `json:"event_ts"`
}
*/

func RespondToMessage(event *slackevents.AppMentionEvent) {
	text := strings.Split(event.Text, " ")

	if !strings.Contains(text[0], BotID) {
		SlackBot.PostMessage(event.Channel, messageNotACommand())
		return
	}

	if len(text) < 2 {
		handleHelp(event)
		return
	}

	switch text[1] {
	default:
		handleHelp(event)
	}
}