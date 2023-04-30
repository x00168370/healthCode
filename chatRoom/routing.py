from channels.routing import ProtocolTypeRouter, URLRouter
from chatRoom.consumers import ChatUser
from django.urls import re_path



websocket_urlpatterns = [
    re_path(r'^ws/(?P<room_name>[^/]+)/$', ChatUser.as_asgi()),
]


application = ProtocolTypeRouter({
    'websocket':
        URLRouter(
            websocket_urlpatterns
        )
    ,
})