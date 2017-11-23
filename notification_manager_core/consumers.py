from django.http import HttpResponse
from channels.handler import AsgiHandler


# def http_request_consumer(message):
#
#     response = HttpResponse(
#         str.format('You asked for {}', message.content['path']))
#
#     for chunk in AsgiHandler.encode_response(response):
#         message.reply_channel.send(chunk)


def ws_message(message):
    # ASGI WebSocket packet-received and send-packet message types
    # both have a "text" key for their textual data.

    print(
        str.format('Received message from fronentd Websocket: {}',
                   message.content['text'])
    )

    message.reply_channel.send({
        "text": "You sent to websocket: " + message.content['text'],
    })


def ws_connect(message):
    pass


def ws_disconnect(message):
    pass
