from django.urls import path
from .consumers import *


websocket_urlpatterns = [
    # chatroom_name is what we store in the chat room table
    # ChatroomConsumer is a class and we initialize it with as_asgi() method
    path('ws/chatroom/<str:chatroom_name>', ChatroomConsumer.as_asgi()),
]