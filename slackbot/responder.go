package slackbot

import (
	"strings"

	"github.com/slack-go/slack"
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
		SlackBot.PostMessage(event.Channel, slack.MsgOptionText("I'm a busy bot. Call me only when you need me. :angry:", false))
		return
	}
	SlackBot.PostMessage(event.Channel, slack.MsgOptionText("Aaryan stupid", false))
}