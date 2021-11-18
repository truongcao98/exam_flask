SLACK_TOKEN = "xoxb-2744748955617-2737087864932-uD9bCWiZ3xKjCf7KG7VriQkd"
import slack
from slack_bolt import App

client = slack.WebClient(token=SLACK_TOKEN)

# channel = "group-consumer-voucher-grant-code-internal"
channel = "random"

client.chat_postMessage(channel="group-consumer-voucher-grant-code-internal",
                        blocks=[
                            {
                                "type": "section",
                                "text": {
                                    "type": "mrkdwn",
                                    "text": "*truongcl:*"
                                }
                            }
                        ]
                        )