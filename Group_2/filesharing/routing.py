 #chat/routing.py
from django.conf.urls import url
from . import consumers

websocket_urlpatterns = [
    # url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.showDatabaseConsumer),
    url(r'^ws/boxoshare/', consumers.Tracker),
]


# import websockets to open a connection with python
# Check what should URL look like for web sockets
