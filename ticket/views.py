from django.shortcuts import render, get_object_or_404
from rest_framework import generics, permissions
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ticket.models import Ticket, Answer, Feedback
from ticket.serializers import TicketSerializer, AnswerSerializer, FeedbackSerializer


class TicketView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        tickets = Ticket.objects.all()
        return Response({'tickets': TicketSerializer(tickets, many=True).data})

    def post(self, request):
        serializer = TicketSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'tickets': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': "method PUT not allowed"})

        try:
            instance = Ticket.objects.get(pk=pk)
        except:
            return Response({'error': "not exist"})

        serializer = TicketSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'tickets': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': "method PUT not allowed"})

        try:
            instance = Ticket.objects.get(pk=pk)
            instance.delete()
            return Response({'status': "delete successful"})
        except:
            return Response({'error': "not exist"})


class AnswerView(APIView):
    def get(self, request):
        answer = Answer.objects.all()
        return Response({'answer': AnswerSerializer(answer, many=True).data})

    def post(self, request):
        serializer = AnswerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(request.data)
        ticket = get_object_or_404(Ticket, id=request.data.get('ticket_id'))
        ticket.status = "done"
        ticket.save()
        return Response({'answer': serializer.data})

class FeedbackView(APIView):
    def get(self, request):
        feedback = Feedback.objects.all()
        return Response({'feedback': FeedbackSerializer(feedback, many=True).data})

    def post(self, request):
        serializer = FeedbackSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(request.data)
        return Response({'feedback': serializer.data})


class TicketsView(APIView):
    def get(self, request):
        tickets = Ticket.objects.all()
        answer = Answer.objects.all()
        feedback = Feedback.objects.all()
        # for
        return Response({'feedback': FeedbackSerializer(feedback, many=True).data,
                        'tickets': TicketSerializer(tickets, many=True).data,
                        'answer': AnswerSerializer(answer, many=True).data})


    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)

