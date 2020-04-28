package slackbot

import (
	"github.com/slack-go/slack"
)

func messageNotACommand() slack.MsgOption {
	return slack.MsgOptionText("I'm a busy bot. Call me only when you need me. :angry:", false)
}

func messageError() slack.MsgOption {
	return slack.MsgOptionText("An error occurred on the server.", false)
}

func messageHelp() slack.MsgOption {
	helpMessage := "Hey! The following commands are supported as of now:\n"
	helpMessage += "`help`, `rating`\n"
	helpMessage += "Syntax: `@tle <command> <options>`"
	return slack.MsgOptionText(helpMessage, false)
}

func messageHelpRating() slack.MsgOption {
	helpMessage := "The `rating` command displays the rating graph of one or more users.\n"
	helpMessage += "Syntax: `@tle rating <users>`"
	return slack.MsgOptionText(helpMessage, false)
}

func messageRating(file string) slack.MsgOption {
	block := slack.ImageBlock{
		Type: slack.MBTImage,
		ImageURL: file,
		AltText: "Image",
		Title: &slack.TextBlockObject{
			Type: "plain_text",
			Text: "Rating graph",
		},
	}
	return slack.MsgOptionBlocks(block)
}