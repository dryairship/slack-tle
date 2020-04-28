package slackbot

import (
	"github.com/slack-go/slack"
)

func messageNotACommand() slack.MsgOption {
	return slack.MsgOptionText("I'm a busy bot. Call me only when you need me. :angry:", false)
}

func messageHelp() slack.MsgOption {
	helpMessage := "Hey! The following commands are supported as of now:\n"
	helpMessage += "`help`, `rating`"
	return slack.MsgOptionText(helpMessage, false)
}