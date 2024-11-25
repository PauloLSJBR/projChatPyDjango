from django.urls import path
from . import views

urlpatterns = [
    path('messages/', views.MessageListView.as_view(), name='message-list'),  # Listar mensagens
    path('messages/send/', views.SendMessageView.as_view(), name='send-message'),  # Enviar mensagem
]