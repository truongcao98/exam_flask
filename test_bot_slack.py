SLACK_TOKEN = "xoxb-2710008378421-2710021655653-UrCdebDFNxEXtnghpybmW90c"
import slack
client = slack.WebClient(token=SLACK_TOKEN)

client.chat_postMessage(channel='#l',
                        blocks=[
                            {
                                "type": "section",
                                "text": {
                                    "type": "mrkdwn",
                                    "text": "_///////////_" + '\n' + "current_time" + '\n' + "* ___Topic hiện tại có :* " + ' tin nhắn lag__: '
                                }
                            }
                        ]
                        )