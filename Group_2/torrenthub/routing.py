from channels.auth import AuthMiddlewareStack
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter, URLRouter
from filesharing.routing import websocket_urlpatterns

application = ProtocolTypeRouter({
'websocket':AuthMiddlewareStack(
	URLRouter(websocket_urlpatterns)
	),
})

# Only websockets are required
# Any http requests will be taken care by django views
# AuthMiddleware stack -> standard django authentication -> stores users details in Sessions
