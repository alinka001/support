from django.contrib import admin
from django.urls import path, include

from ticket.views import TicketView, AnswerView, FeedbackView, TicketsView

urlpatterns = [
    path('ticket/', TicketView.as_view()),
    path('ticket//<int:pk>', TicketView.as_view()),
    path('answer/', AnswerView.as_view()),
    path('feedback/', FeedbackView.as_view()),
    path('tickets/', TicketsView.as_view()),
]
