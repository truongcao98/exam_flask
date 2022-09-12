import json
import traceback
import logging
import slack

SLACK_TOKEN = "xoxb-2958143458371-3965989468720-iqIb7Iz3L4P015xlZYwnY3Pf"
client = slack.WebClient(token=SLACK_TOKEN)


# channel = "group-consumer-voucher-grant-code-internal"
class MonitorKafkaLogging:

    @staticmethod
    def send_error(func_name, exception):
        vm_type = 'LOCAL'
        error = 'Máy chủ: ' + str(vm_type) + ' \n' + 'In function: ' + str(func_name) + ": " + str(exception) + '\n'
        client.chat_postMessage(channel='#log',
                                blocks=[
                                    {
                                        'type': 'section',
                                        'text': {
                                            'type': 'mrkdwn',
                                            'text': str(error)
                                        }
                                    }
                                ]
                                )


if __name__ == '__main__':
    try:
        a = 1 / 0
    except Exception as e:
        # log_traceback(e)
        # logger.error(ex, exc_info=True)
        tb = traceback.format_exc()
        # logging.critical(e, exc_info=True)
        MonitorKafkaLogging.send_error('truongcl', tb)
