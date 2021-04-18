from django.urls import path
from .views import (
    MessageListView,
    MessageSentListView,
    MessageDetailView,
    MessageCreateView,
    MessageReplyView,
    MessageDeleteView,
)
from . import views

app_name = 'messaging'

urlpatterns = [
    path('messages/', MessageListView.as_view(), name='messages-received'),
    path('messages/sent/', MessageSentListView.as_view(), name='messages-sent'),
    path('message/<int:pk>/', MessageDetailView.as_view(), name='message-detail'),
    path('message/<int:pk>/reply/', MessageReplyView.as_view(), name='message-reply'),
    path('message/<int:pk>/delete/', MessageDeleteView.as_view(), name='message-delete'),
    path('message/new/', MessageCreateView.as_view(), name='message-create'),

    path('search/', views.search, name='search')
]
