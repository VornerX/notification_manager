from channels.routing import route
from notification_manager_core.consumers import ws_message


channel_routing = [
    route("websocket.receive", ws_message),
]

# channel_routing = [
#     route(
#         'http.request',
#         'interaction_point_core.consumers.http_request_consumer'
#     )
# ]
