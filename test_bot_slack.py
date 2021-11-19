import json

SLACK_TOKEN = "xoxb-2744748955617-2737087864932-AewPYSfSeDhwRmzNpurBHMOE"
import slack

client = slack.WebClient(token=SLACK_TOKEN)

# channel = "group-consumer-voucher-grant-code-internal"
channel = "random"

intro_msg = json.dumps([{
    "fallback": "Warning! Have topic lag",
    # "color": "#fc0511",
    "color": "#fab905",
    "pretext": "Description info topic lag",
    "fields": [
        # {
        #     "value": "* _______ **17:59 18/11/2021** _______ *",
        # },
        {
            "value": "*Topic*: voucher-internal-grant-code-profile   *Partition*: `0`   *Lag*: `2984`",
        },
        {
            "value": "Số lượng lag giảm: 0",
        }
    ],
    "footer": "Will be smart",
    "footer_icon": "https://media-exp1.licdn.com/dms/image/C510BAQHkgTAhiRQjRw/company-logo_200_200/0/1565949926495?e=2159024400&v=beta&t=704xlUQlIZ9Nr3QmBjXOEXKhCUQr0gcnGdmD9LUjILA",

}])
client.chat_postMessage(channel="group-consumer-voucher-grant-code-internal",
                        attachments=intro_msg
                        )
