import json

SLACK_TOKEN = "xoxb-2744748955617-2737087864932-qBzGcOnr1eAsQtdzj10ZKJch"
import slack

client = slack.WebClient(token=SLACK_TOKEN)

# channel = "group-consumer-voucher-grant-code-internal"
channel = "random"

intro_msg = json.dumps([{
    "fallback": "Plain-text summary of the attachment.",
    # "color": "#fc0511",
    "color": "#fab905",
    "pretext": "Optional text that appears above the attachment block",
    "author_name": "Bobby Tables",
    "text": "Optional text that appears within the attachment",
    "fields": [
        {
            "title": "Priority",
            "value": "High",
            "short": False
        }
    ],
    "footer": "Slack API",
    "footer_icon": "https://platform.slack-edge.com/img/default_application_icon.png",
    "ts": 123456789
}])

client.chat_postMessage(channel="group-consumer-voucher-grant-code-internal",
                        blocks=[
                            {
                                "type": "section",
                                "text": {
                                    "type": "mrkdwn",
                                    "text": "*truongcl:*"
                                }
                            }
                        ],
                        attachments=intro_msg
                        )
