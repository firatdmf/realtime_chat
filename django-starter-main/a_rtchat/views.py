from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required 
from .models import *

# Create your views here.

@login_required
def chat_view(request):
    # Get all messages belong to this group
    chat_group = get_object_or_404(ChatGroup, group_name='public-chat')
    # Get the last 30 messages
    chat_messages = chat_group.chat_messages.all()[:30]
    return render(request, 'a_rtchat/chat.html', {'chat_messages': chat_messages})