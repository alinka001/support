from django.shortcuts import render, get_object_or_404
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from ticket.models import Ticket, Answer, Feedback
from ticket.serializers import TicketSerializer, AnswerSerializer, FeedbackSerializer, CombinedSerializer


class TicketView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.is_employee:
            tickets = Ticket.objects.all()
        else:
            tickets = Ticket.objects.filter(author=request.user)
        return Response({'tickets': TicketSerializer(tickets, many=True).data})

    def post(self, request):
        if not request.user.is_employee:
            return Response({'error': 'Работники не могут создавать заявки'})
        serializer = TicketSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)

        return Response({'tickets': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': "Метод PUT запрещён"})

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
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        answer = Answer.objects.all()
        return Response({'answer': AnswerSerializer(answer, many=True).data})

    def post(self, request):
        if not request.user.is_employee:
            return Response({'error': 'Пользователи не могут отвечать на заявки'})
        serializer = AnswerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(request.data)
        ticket = get_object_or_404(Ticket, id=request.data.get('ticket_id'))
        ticket.status = "done"
        ticket.save()
        return Response({'answer': serializer.data})


class FeedbackView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        feedback = Feedback.objects.all()
        return Response({'feedback': FeedbackSerializer(feedback, many=True).data})

    def post(self, request):
        if request.user.is_employee:
            return Response({'error': 'Работники не могут оставлять фидбэк'})
        serializer = FeedbackSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(request.data)
        return Response({'feedback': serializer.data})


class TicketsView(ListAPIView):
    serializer_class = CombinedSerializer

    def get_queryset(self):
        data = []
        tickets = Ticket.objects.all()
        answers = Answer.objects.all()
        for ticket in tickets:
            answer = answers.filter(ticket_id=ticket.id).first()
            data.append({'ticket': ticket, 'answer': answer})

        return data




