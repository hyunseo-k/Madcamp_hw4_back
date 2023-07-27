from django.urls import re_path

from . import consumers
from .consumer.drawboard_consumer import DrawboardConsumer

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
    re_path(r'ws/drawboard/(?P<drawboard_id>\w+)/$', DrawboardConsumer.as_asgi()),
] 