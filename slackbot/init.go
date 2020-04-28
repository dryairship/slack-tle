package slackbot

import (
	"os"

	"github.com/slack-go/slack"
)

var SlackBot *slack.Client
var BotID string
var BotName string

func init() {
	botToken := os.Getenv("SLACK_BOT_TOKEN")
	SlackBot = slack.New(botToken)
	response, err := SlackBot.AuthTest()
	if err != nil {
		panic(err)
	}
	BotID = response.UserID
	BotName = response.User
}