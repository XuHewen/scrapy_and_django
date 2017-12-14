from django.shortcuts import render
from .models import UserMessage


# Create your views here.
def get_form(request):
    user_message = UserMessage()

    if request.method == 'POST':
        name = request.POST.get('name', '')
        address = request.POST.get('address', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        user_message.name = name
        user_message.email = email
        user_message.address = address
        user_message.message = message

        user_message.save()

    return render(request, 'index.html')
