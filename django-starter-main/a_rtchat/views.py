from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required 
from .models import *
from .forms import ChatmessageCreateForm
# Create your views here.

@login_required
def chat_view(request):
    # Get all messages belong to this group
    chat_group = get_object_or_404(ChatGroup, group_name='public-chat')
    # Get the last 30 messages
    chat_messages = chat_group.chat_messages.all()[:30]
    form = ChatmessageCreateForm()
    # if request.method == 'POST':
    if request.htmx:
        form = ChatmessageCreateForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.group = chat_group
            message.save()
            context = {'message': message, 'user': request.user}
            return render(request, 'a_rtchat/partials/chat_message_p.html', context )


    return render(request, 'a_rtchat/chat.html', {'chat_messages': chat_messages, 'form': form})


